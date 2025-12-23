from address import Address


class Mailing:
    def __init__(
        self,
        to_address: Address,
        from_address: Address,
        cost: int,
    ) -> None:
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost

    def print_mailing_info(self) -> None:
        print("Отправление:")
        print("Откуда:")
        self.from_address.print_address()
        print("Куда:")
        self.to_address.print_address()
        print(f"Стоимость: {self.cost} руб.")
