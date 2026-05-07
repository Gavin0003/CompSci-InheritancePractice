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
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

class Car(automobile):
    def __init__(self, make, model, mileage, price, doors):
        super().__init__(make, model, mileage, price)
        self.__doors = doors
    def set_doors(self, num_door):
        self.__doors = num_door
    def get_variable(self):
        return self.__doors
    def get_name(self):
        return 'car'
    def get_var(self):
        return 'Number of doors'
class Truck(automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        super().__init__(make, model, mileage, price)
        self.__drive_type = drive_type 
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
    def get_variable(self):
        return self.__drive_type
    def get_name(self):
        return 'truck'
    def get_var(self):
        return 'Drive type'
class SUV(automobile):
    def __init__(self, make, model, mileage, price, passenger_capacity):
        super().__init__(make, model, mileage, price)
        self.__passenger_capacity = passenger_capacity 
    def set_passenger_capacity(self, passenger_capacity):
        self.__passenger_capacity = passenger_capacity
    def get_variable(self):
        return self.__passenger_capacity
    def get_name(self):
        return 'suv'
    def get_var(self):
        return 'Passenger capacity'