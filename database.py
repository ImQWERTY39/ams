from mysql.connector import connect

database, cursor = None, None

def init(username: str, password: str) -> bool:
    global database, cursor
    try: database = connect(host="localhost", user=username, password=password)
    except: return False

    cursor = database.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS apt")
    cursor.execute("USE apt")
    cursor.execute("CREATE TABLE IF NOT EXISTS owner_detail( name VARCHAR(50) PRIMARY KEY,\
        phno CHAR(10) UNIQUE NOT NULL, email VARCHAR(50) UNIQUE NOT NULL, houses_owned TINYINT(2) UNSIGNED NOT NULL)")
    cursor.execute("CREATE TABLE IF NOT EXISTS flat_detail( flat_number VARCHAR(20) PRIMARY KEY,\
        availability BOOL NOT NULL, for_rent BOOL NOT NULL, owner_name VARCHAR(50),\
        tenant_name VARCHAR(50), FOREIGN KEY (owner_name) REFERENCES owner_detail(name) ON UPDATE CASCADE) ")

    return True

def close() -> None:
    global database, cursor
    try: cursor.close(); database.close()
    except AttributeError: pass
    finally: database, cursor = None, None

def add_flat(fn, avail, rent, owner, tenant, phno, email):
    owned, rented, owner_exists = rent or (not avail), rent and (not avail), get_owner(owner) is not None
    
    if fn == "": return 1
    if get_flat(fn) is not None: return 2
    if owned:
        if owner == "": return 3
        if not owner_exists:
            if not phno.isdigit() or len(phno) != 10: return 4
            if len(list(filter(lambda x: len(x) > 0, email.split('@')))) != 2: return 5
            cursor.execute(f"INSERT INTO owner_detail VALUES ('{owner}', '{phno}', '{email}', 1)")
        else: cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned + 1 WHERE name = '{owner}'")
    else: owner = None
    if rented and tenant == "": return 6
    if not rented: tenant = None

    cursor.execute("INSERT INTO flat_detail VALUES (%s, %s, %s, %s, %s)", (fn, avail, rent, owner, tenant))
    database.commit()
    
def get_flat(fn):
    cursor.execute(f"SELECT * FROM flat_detail WHERE flat_number = '{fn}'")
    res = cursor.fetchall()
    return None if len(res) == 0 else res[0]

def get_flats():
    cursor.execute("SELECT * FROM flat_detail")
    return cursor.fetchall()

def get_owner(owner):
    cursor.execute(f"SELECT * FROM owner_detail WHERE name = '{owner}'")
    res = cursor.fetchall()
    return None if len(res) == 0 else res[0]

def get_owners():
    cursor.execute("SELECT * FROM owner_detail")
    return cursor.fetchall()

def delete_flat(flat):
    if flat[3] is not None: owner = get_owner(flat[3])
    else: owner = None
    cursor.execute(f"DELETE FROM flat_detail WHERE flat_number = '{flat[0]}'")
    if owner is not None:
        if owner[3] == 1: delete_owner(owner[0])
        else: cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned - 1 WHERE name = '{owner[0]}'")
    database.commit()
    return owner

def delete_owner(owner):
    cursor.execute(f"DELETE FROM owner_detail WHERE name = '{owner}'")
    database.commit()

def update_owner(old_owner_info, new_owner_info):
    if get_owner(new_owner_info[0]) is not None: return 1
    cursor.execute(f"UPDATE owner_detail SET name = '{new_owner_info[0]}', phno = '{new_owner_info[1]}',\
                   email = '{new_owner_info[2]}' WHERE name = '{old_owner_info[0]}'")
    database.commit()

def rent_out_flat(flat_number, tenant_name):
    if tenant_name == '': return 1
    cursor.execute(f"UPDATE flat_detail SET tenant_name = '{tenant_name}', availability = 0 WHERE flat_number = '{flat_number}'")
    database.commit()

def buy_flat(flat_number, owner_name, phno, email):
    if owner_name == '': return 1
    owner = get_owner(owner_name)
    if owner is not None: cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned + 1 WHERE name = '{owner_name}'")
    else:
        if not phno.isdigit() or len(phno) != 10: return 2
        if len(list(filter(lambda x: len(x) > 0, email.split('@')))) != 2: return 3
        cursor.execute(f"INSERT INTO owner_detail VALUES ('{owner_name}', '{phno}', '{email}', 1)")
    cursor.execute(f"UPDATE flat_detail SET owner_name = '{owner_name}', availability = 0 WHERE flat_number = '{flat_number}'")
    database.commit()

def sell_flat(flat, owner):
    ret = False
    if flat[2]: cursor.execute(f"UPDATE flat_detail SET availability = 1, tenant_name = NULL WHERE flat_number = '{flat[0]}'")
    else:
        cursor.execute(f"UPDATE flat_detail SET availability = 1, owner_name = NULL WHERE flat_number = '{flat[0]}'")
        if owner[3] > 1: cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned - 1 WHERE name = '{owner[0]}'")
        else: delete_owner(owner[0]); ret = True
    database.commit(); return ret

def get_flats_count():
    cursor.execute(f"SELECT COUNT(*) FROM flat_detail")
    return cursor.fetchall()[0][0]

def get_flats_for_sale_count():
    cursor.execute(f"SELECT COUNT(*) FROM flat_detail WHERE availability = 1 AND for_rent = 0")
    return cursor.fetchall()[0][0]

def get_flat_for_rent_count():
    cursor.execute(f"SELECT COUNT(*) FROM flat_detail WHERE availability = 1 AND for_rent = 1")
    return cursor.fetchall()[0][0]

def get_occupied_flat_count():
    cursor.execute(f"SELECT COUNT(*) FROM flat_detail WHERE availability = 0")
    return cursor.fetchall()[0][0]
