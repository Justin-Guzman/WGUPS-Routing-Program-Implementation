from datetime import timedelta

class Package:
    
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        """
        Initialize a Package object with its details.
        Each package holds its unique information, such as address, deadline, weight, and status.
        """
        self.package_id = package_id
        self.original_address = address  # Store the original address to avoid modification
        self.address = address           # Current address (may change under certain conditions)
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline         # Deadline for package delivery
        self.weight = weight             # Weight of the package
        self.status = status             # Current status of the package
        self.departure_time = None       # Time when the package departs
        self.delivery_time = None       # Time when the package is delivered

    def update_status(self, current_time):
        """
        Return a string representation of the package's status at a given time.
        This method does not modify the package object itself.
        
        The status reflects whether the package is at the hub, en route, or delivered based on the time passed.
        """
        # Determine if we should use the corrected address for a specific package (e.g., package 9)
        address_to_use = self.original_address
        if self.package_id == 9 and current_time >= timedelta(hours=10, minutes=20):  # Special case for package 9
            address_to_use = "410 S State St"  # Address correction

        # Check the status based on whether the package is delivered, en route, or still at the hub
        if self.delivery_time and self.delivery_time < current_time:
            status = f"Delivered at {self.delivery_time}."  # Delivered
        elif self.departure_time and self.departure_time <= current_time:
            status = f"En Route at {current_time}."  # On the way
        else:
            status = f"At The Hub at {current_time}."  # Package still at the hub

        # Return a string representation of the package's current state, including all relevant details
        return f'ID: {self.package_id}; Address: {address_to_use}, {self.city}, {self.state}, {self.zip_code}; Deadline: {self.deadline}; Weight: {self.weight}; {status}'

    def __str__(self):
        """
        Return a string representation of the package's current state.
        This includes the address, deadline, weight, and status, along with delivery time if applicable.
        """
        return f'ID: {self.package_id}; Address: {self.address}, {self.city}, {self.state}, {self.zip_code}; Deadline: {self.deadline}; Weight: {self.weight}, {self.status} at {self.delivery_time}.'
