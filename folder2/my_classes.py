
class Car:
    def __init__(self, brand):
        self.brand = brand


class Brand(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand)
        self.model = model
        self.color = color


class Quantity(Brand):
    def __init__(self, brand, model, color, quantity):
        super().__init__(brand, model, color)
        self.quantity = quantity

    def check_quantity(self):
        print(f"There are { self.quantity, self.color, self.brand, self.model} on stock")
