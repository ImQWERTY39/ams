from mysql.connector import connect

database, cursor = None, None

def init(username, password):
    global database, cursor
    try: database = connect(host="localhost", user=username, password=password)
    except: return False

    cursor = database.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS apt")
    cursor.execute("USE apt")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS owner_detail (
    name VARCHAR(100) NOT NULL,
    phno CHAR(10) PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    houses_owned TINYINT(2) UNSIGNED NOT NULL DEFAULT 1
)""")
    cursor.execute("""
CREATE TABLE IF NOT EXISTS flat_detail (
    flat_number VARCHAR(20) PRIMARY KEY,
    availability BOOL NOT NULL,
    for_rent BOOL NOT NULL,
    owner_phno CHAR(10),
    tenant_name VARCHAR(100),
    FOREIGN KEY (owner_phno) REFERENCES owner_detail(phno) ON UPDATE CASCADE
)""")

    return True

def close():
    global database, cursor
    try: cursor.close(); database.close()
    except AttributeError: pass
    finally: database, cursor = None, None

def add_flat(flat_number, availability, for_rent, owner, tenant, phno, email):
    if flat_number == "": return 1
    if get_flat(flat_number) is not None: return 2

    owned = for_rent or (not availability)
    rented = for_rent and (not availability)
    owner_exists = get_owner(phno) is not None if is_valid_phno(phno) else False

    if owned:
        if owner == "": return 3
        if not owner_exists:
            if not is_valid_phno(phno): return 4
            if not is_valid_email(email): return 5
            if not is_unique_email(email): return 6

            cursor.execute(f"INSERT INTO owner_detail VALUES ('{owner}', '{phno}', '{email}', 1)")
        else:
            cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned + 1 WHERE owner_phno = '{phno}'")
    else:
        phno = None

    if rented and tenant == "": return 7
    if not rented: tenant = None

    cursor.execute("INSERT INTO flat_detail VALUES (%s, %s, %s, %s, %s)",
        (flat_number, availability, for_rent, phno, tenant))
    database.commit()

def get_flat(flat_number):
    cursor.execute(f"SELECT * FROM flat_detail WHERE flat_number = '{flat_number}'")
    res = cursor.fetchall()
    return None if len(res) == 0 else res[0]

def get_flats():
    cursor.execute(f"SELECT * FROM flat_detail")
    return cursor.fetchall()

def get_owner(phno):
    cursor.execute(f"SELECT * FROM owner_detail WHERE phno = '{phno}'")
    res = cursor.fetchall()
    return None if len(res) == 0 else res[0]

def get_owners():
    cursor.execute(f"SELECT * FROM owner_detail")
    return cursor.fetchall()

def delete_flat(flat):
    owner = get_owner(flat[3]) if flat[3] is not None else None
    cursor.execute(f"DELETE FROM flat_detail WHERE flat_number = '{flat[0]}'")

    if owner is not None:
        if owner[3] == 1: delete_owner(owner[1])
        else:
            cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned - 1 WHERE phno = '{owner[1]}'")

    database.commit()
    return owner

def delete_owner(phno):
    cursor.execute(f"DELETE FROM owner_detail WHERE phno = '{phno}'")
    database.commit()

def update_owner(ooi, noi):
    if not is_valid_phno(noi[1]): return 1
    if not is_valid_email(noi[2]): return 2
    if ooi[1] != noi[1] and not is_unique_phno(noi[1]): return 3
    if ooi[2] != noi[2] and not is_unique_phno(noi[2]): return 4

    cursor.execute(f"UPDATE owner_detail SET name = '{noi[0]}', \
        phno = '{noi[1]}', email = '{noi[2]}' WHERE phno = '{ooi[1]}'")
    database.commit()

def rent_out_flat(flat_number, tenant_name):
    if tenant_name == "": return 1
    cursor.execute(f"UPDATE flat_detail SET tenant_name = '{tenant_name}', availability = 0 WHERE flat_number = '{flat_number}'")
    database.commit()

def buy_flat(flat_number, owner_name, phno, email):
    if not is_valid_phno(phno): return 1
    owner = get_owner(phno)

    if owner is not None:
        cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned + 1 WHERE phno = '{phno}'")
    else:
        if owner_name == "": return 2
        if not is_valid_email(email): return 3
        if not is_unique_email(email): return 4

        cursor.execute(f"INSERT INTO owner_detail VALUES ('{owner_name}', '{phno}', '{email}', 1)")

    cursor.execute(f"UPDATE flat_detail SET owner_phno = '{phno}',\
        availability = 0 WHERE flat_number = '{flat_number}'")
    database.commit()

def sell_flat(flat, owner):
    owner_deleted = False

    if flat[2]:
        cursor.execute(f"UPDATE flat_detail SET availability = 1, tenant_name = NULL WHERE flat_number = '{flat[0]}'")
    else:
        cursor.execute(f"UPDATE flat_detail SET availability = 1, owner_phno = NULL WHERE flat_number = '{flat[0]}'")

        if owner[3] > 1:
            cursor.execute(f"UPDATE owner_detail SET houses_owned = houses_owned - 1 WHERE phno = '{owner[1]}'")
        else:
            delete_owner(owner[1])
            owner_deleted = True

    database.commit()
    return owner_deleted

def modify_flat(flat, new_avail, new_for_rent, new_tenant):
    owned = new_for_rent or (not new_avail)
    rented = new_for_rent and (not new_avail)

    if not owned: return 1
    if not rented: new_tenant = None
    elif new_tenant == "": return 2

    
    cursor.execute("UPDATE flat_detail SET availability = %s, for_rent = %s, tenant_name = %s WHERE flat_number = %s", 
                   (new_avail, new_for_rent, new_tenant, flat[0]))
    database.commit()


def get_flats_count():
    cursor.execute("SELECT COUNT(*) FROM flat_detail")
    return cursor.fetchall()[0][0]

def get_flats_for_sale_count():
    cursor.execute("SELECT COUNT(*) FROM flat_detail WHERE availability = 1 AND for_rent = 0")
    return cursor.fetchall()[0][0]

def get_flat_for_rent_count():
    cursor.execute("SELECT COUNT(*) FROM flat_detail WHERE availability = 1 AND for_rent = 1")
    return cursor.fetchall()[0][0]

def get_occupied_flat_count():
    cursor.execute("SELECT COUNT(*) FROM flat_detail WHERE availability = 0")
    return cursor.fetchall()[0][0]

def is_valid_email(email):
    return len(list(filter(lambda x: len(x) > 0, email.split('@')))) == 2

def is_valid_phno(phno):
    return phno.isdigit() and len(phno) == 10

def is_unique_phno(phno):
    cursor.execute("SELECT phno FROM owner_detail")
    phnos = cursor.fetchall()
    return (phno,) not in phnos

def is_unique_email(email):
    cursor.execute("SELECT email FROM owner_detail")
    emails = cursor.fetchall()
    return (email,) not in emails
