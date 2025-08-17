"""A class that can be used to represent a car."""

class Car:
    """A class that represents a car."""
    
    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Return the car's odometer reading."""
        return self.odometer_reading

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increment the odometer reading by a given amount."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment by a negative value!")