
import my_classes

if __name__ == '__main__':

    car1 = my_classes.Quantity("AUDI", "A3", "red")

    car1.check_quantity()
    car1.sell_car()
    car1.check_quantity()

    car2 = my_classes.Quantity("BMW", "5", "black")
    car2.check_quantity()

    car2.brand = 123
    car2.check_quantity()



