class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.__brand},{self.__model}"

    def get__brand(self):
        return self.__brand + " !"

    def fuel_type(self):
        return "diesel or petrol fuel type"



    # using @staticmethod decorator we can protect the property of the class and we have to cut off the wiring by removing self keyword from the property of the class
    # by using decorator static the stance of the class cannot access the static property directly

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    # it hides the property of the class and cannot override the property if we want to not change the property then we use property decorator
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)

    def electric_car(self):
        return f"Electric Car,{self.__brand},{self.__model},{self.battery_size}"

    def fuel_type(self):
        return "Electric fuel type"

my_tesla = ElectricCar('tesla', 'model S', '200KWh')
print(my_tesla.get__brand())

print(my_tesla.fuel_type())

safari = Car("tata","safari")
safari3 = Car("tata","safari3")
nexon = Car("tata","nexon")
# my_tesla.model = "fortuner"
print(my_tesla.general_description())
print(Car.general_description())
print(my_tesla.model)


