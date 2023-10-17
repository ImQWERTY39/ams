class FlatInfo:
    availability: bool
    on_rent: bool
    owner_name: str
    tenant_name: str

    def __init__(
        self,
        availability: bool,
        on_rent: bool,
        owner_name: str,
        tenant_name: str,
    ) -> None:
        self.availability = availability
        self.on_rent = on_rent
        self.owner_name = owner_name
        self.tenant_name = tenant_name

    def to_dict(self) -> dict:
        return {
            "availability": self.availability,
            "on_rent": self.on_rent,
            "owner_name": self.owner_name,
            "tenant_name": self.tenant_name,
        }

    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(
            dictionary["availability"],
            dictionary["on_rent"],
            dictionary["owner_name"],
            dictionary["tenant_name"],
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
