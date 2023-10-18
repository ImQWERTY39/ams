class FlatInfo:
    availability: bool
    on_rent: bool
    _owner_name: str
    _tenant_name: str

    def __init__(
        self,
        availability: bool,
        on_rent: bool,
        owner_name: str,
        tenant_name: str,
    ) -> None:
        self.availability = availability
        self.on_rent = on_rent
        self._owner_name = owner_name if owner_name else None
        self._tenant_name = tenant_name if owner_name else None

    def to_dict(self) -> dict:
        return {
            "availability": self.availability,
            "on_rent": self.on_rent,
            "owner_name": self._owner_name,
            "tenant_name": self._tenant_name,
        }

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(
            dictionary["availability"],
            dictionary["on_rent"],
            dictionary["owner_name"],
            dictionary["tenant_name"],
        )

    @property
    def owner_name(self):
        if self.on_rent or (not self.availability):
            return self._owner_name
        else:
            return None

    @property
    def tenant_name(self):
        if self.on_rent and (not self.availability):
            return self._tenant_name
        else:
            return None

    @owner_name.setter
    def owner_name(self, new_owner_name: str):
        if self.on_rent or (not self.availability):
            self._owner_name = (
                new_owner_name.strip().upper() if new_owner_name is not None else None
            )

    @tenant_name.setter
    def tenant_name(self, new_tenant_name: str):
        if self.on_rent and (not self.availability):
            self._tenant_name = (
                new_tenant_name.strip().upper() if new_tenant_name is not None else None
            )


class OwnerInfo:
    phone_number: str
    email: str
    flats_owned: list[str]

    def __init__(
        self,
        phone_number: str,
        email: str,
        flats_owned: list[str],
    ) -> None:
        self.phone_number = phone_number
        self.email = email
        self.flats_owned = flats_owned

    def to_dict(self) -> dict:
        return {
            "phone_number": self.phone_number,
            "email": self.email,
            "flats_owned": self.flats_owned,
        }

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(
            dictionary["phone_number"],
            dictionary["email"],
            dictionary["flats_owned"],
        )
