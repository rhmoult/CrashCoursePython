from car import Car

my_new_car = Car("Audi", "Q3", 2022)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 0
my_new_car.read_odometer()

