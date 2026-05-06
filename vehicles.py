'doors'
'wheels'
'engine'
class automobile:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price


    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__ = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

car = automobile("Gavin Pettit", "123 Maple St, Seattle, WA", 28, "555-666-7777")
print(car.get_make())