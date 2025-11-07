class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def full_name(self):
        return f"{self.__brand},{self.model}"

    def get__brand(self):
        return self.__brand + " !"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)

    def electric_car(self):
        return f"Electric Car,{self.__brand},{self.model},{self.battery_size}"

my_tesla = ElectricCar('tesla', 'model S', '200KWh')
print(my_tesla.get__brand())