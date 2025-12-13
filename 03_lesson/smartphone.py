class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    def print_info(self):
        print(f"{self.brand} - {self.model}. {self.phone_number}")
