
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.brand]

    def __set__(self, instance, value):

        if not isinstance(value, str):
            raise TypeError('Oczekiwano łańcucha znaków')
        instance.__dict__[self.brand] = value


class Brand(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand)
        self.model = model
        self.color = color


class Quantity(Brand):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.__quantity = 100

    def check_quantity(self):
        print(f"There are { self.__quantity, self.color, self.brand, self.model} on stock")

    def sell_car(self):
        self.__quantity -= 1
