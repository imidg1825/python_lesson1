class Address:
    def __init__(self, city: str, street: str, house: str, apartment: str):
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def print_address(self) -> None:
        print(
            f"г. {self.city}, ул. {self.street}, д. {self.house}, кв. {self.apartment}"
        )
