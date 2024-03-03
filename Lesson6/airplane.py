class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def print_info(self):
        print(self.name)
        print(self.max_speed)


class Plane(TransportVehicle):

    def __init__(self, name, max_speed, fly_dist):
        super().__init__(name, max_speed)
        self.fly_dist = fly_dist

    def print_info(self):
        super().print_info()
        print(self.fly_dist)


plane = Plane("Plane", 1200, 13000)
plane.print_info()
