from smartphone import Smartphone

phones = [
    Smartphone("Apple", "iPhone 15", "+79990000001"),
    Smartphone("Samsung", "Galaxy S23", "+79990000002"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79990000003"),
    Smartphone("Google", "Pixel 8", "+79990000004"),
    Smartphone("Huawei", "P60", "+79990000005"),
]

for phone in phones:
    phone.print_info()
