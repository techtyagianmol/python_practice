class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"car,{self.brand} {self.model}"


class ElectricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

    def electric_car(self):
        return f"Electric car {self.brand} {self.model},{self.battery_size}"




my_tesla = ElectricCar('tesla', 'model S',"90KWh")
print(my_tesla.full_name())
print(my_tesla.electric_car())