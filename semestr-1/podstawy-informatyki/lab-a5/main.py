from car import *

car1 = Car(4, 2137, "yellow", 5)
car2 = Car(4, 250, "red", 2)
car3 = Car(6, 120, "grey", 3)

car1.seats_set(4)
car2.max_velocity_set(260)
car3.seats_set(4)

electric1 = Electric(4, 210, "white", 5)
electric1.acceleration_set(50)
electric1.autonomic_set(False)
electric1.battery_capacity_set(2500)
print(electric1.wheels_get())

electric1.print_params()