from address import Address
from mailing import Mailing


to_address = Address(
    city="Москва",
    street="Тверская",
    house="1",
    apartment="10",
)

from_address = Address(
    city="Санкт-Петербург",
    street="Невский проспект",
    house="100",
    apartment="25",
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350,
)

mailing.print_mailing_info()
