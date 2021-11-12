class Car:
    def __init__(self, wheels, max_velocity, color, seats):
        self.wheels = wheels
        self.max_velocity = max_velocity
        self.color = color
        self.seats = seats

    # getters
    def wheels_get(self):
        return self.wheels

    def max_velocity_get(self):
        return self.max_velocity

    def color_get(self):
        return self.color

    def seats_get(self):
        return self.seats

    # setters
    def wheels_set(self, wheels):
        self.wheels = wheels

    def max_velocity_set(self, max_velocity):
        self.max_velocity = max_velocity

    def color_set(self, color):
        self.color = color

    def seats_set(self, seats):
        self.seats = seats


class Electric(Car):
    def battery_capacity_set(self, capacity):
        self.battery_capacity = capacity
    
    def battery_capacity_get(self):
        return self.battery_capacity

    def autonomic_set(self, is_autonomic):
        self.autonomic = is_autonomic

    def autonomic_get(self):
        return self.autonomic
    
    def acceleration_set(self, acceleration):
        self.acceleration = acceleration

    def acceleration_get(self):
        return self.acceleration

    def print_params(self):
        print("Color:", self.color)
        print("Wheels:", self.wheels)
        print("Maximum velocity:", self.max_velocity)
        print("Seats:", self.seats)
        print("Battery capacity:", self.battery_capacity)
        print("Is autonomic:", self.autonomic)
        print("Acceleration:", self.acceleration)