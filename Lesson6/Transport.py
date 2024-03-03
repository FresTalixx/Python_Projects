class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def print_info(self):
        print(self.name)
        print(self.max_speed)


car = TransportVehicle("Car", 220)
car.print_info()