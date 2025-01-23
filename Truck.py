# Truck class to represent each delivery truck
class Truck:
    def __init__(self, packages=None, depart_time=None, capacity=16, speed=18, mileage=0.0, address="4001 South 700 East"):
        """
        Initialize a Truck object with its details.
        The truck has attributes such as capacity, speed, load, mileage, address, departure time, and current time.
        The default capacity is 16 packages, speed is 18 mph, and mileage is initially 0.0 miles.
        """
        self.capacity = capacity  # Maximum number of packages the truck can carry
        self.speed = speed        # Speed of the truck in miles per hour
        self.load = 0             # Default load is 0 when initialized (no packages yet)
        self.packages = packages if packages is not None else []  # List of packages in the truck
        self.mileage = mileage   # Total mileage of the truck (initially set to 0)
        self.address = address   # Truck's current address (default is "4001 South 700 East")
        self.depart_time = depart_time  # The time the truck will depart from its location
        self.time = depart_time  # Current time, initialized to departure time

    def __str__(self):
        """
        Return a string representation of the truck's current state.
        This includes details like the truck's capacity, speed, load, mileage, address, departure time, and current time.
        """
        return f"Capacity: {self.capacity}, Speed: {self.speed} mph, Load: {self.load}, Mileage: {self.mileage} miles, Address: {self.address}, Departure Time: {self.depart_time}, Current Time: {self.time}"
