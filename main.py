# Student ID 011119256
# Justin Guzman 
# Wgu C950 DSA Task 2
import csv
from datetime import datetime, timedelta

# Import custom classes for package, truck, and hash table
from HashTable import HashTable
from Package import Package
from Truck import Truck

# Load distance and address data
with open("data/distance-matrix.csv") as dist, open("data/address-table.csv") as addy:
    distance_csv = list(csv.reader(dist))  # Distance matrix between addresses
    address_csv = list(csv.reader(addy))  # Address data mapping

# Read and create Package objects, then load them into the hash table
with open("data/package-file.csv") as pkg:
    pkg_hash = HashTable()
    for package in (Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], "at the hub")
                    for row in csv.reader(pkg)):
        # Insert each package into the hash table using its package ID as the key
        pkg_hash.insert(package.package_id, package)

# Function to get distance between two addresses
def get_distance(addy1, addy2):
    """
    Get the distance between two addresses.
    If the direct distance is not found, check the reverse.
    """
    distance = distance_csv[addy1][addy2] or distance_csv[addy2][addy1]  # Try reverse in case data is not symmetric
    return float(distance)

# Function to get the index for an address
def get_index(address):
    """
    Extract the address index from the string literal of an address.
    Returns the index (as an integer) if found, otherwise returns None.
    """
    for row in address_csv:
        if address in row[2]:  # Look for the address in the address table
            return int(row[0])  # Return the index of the address
    return None  # Return None if address not found

# Initialize truck objects with assigned packages
truck1 = Truck([1, 2, 4, 5, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], timedelta(hours=8))
truck2 = Truck([3, 6, 18, 25, 28, 32, 36, 38], timedelta(hours=9, minutes=5))
truck3 = Truck([7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39], timedelta(hours=10, minutes=20))
trucks = [truck1, truck2, truck3]

def nearest_neighbor(truck):
    """
    Orders packages on a given truck using the nearest neighbor algorithm.
    Also calculates the distance the truck drives once the packages are sorted.
    The nearest neighbor algorithm works by always choosing the closest unvisited package
    as the next stop, based on the current truck's location.
    """
    not_delivered = [pkg_hash.lookup(pkg_id) for pkg_id in truck.packages]  # Get list of packages to be delivered

    truck.packages.clear()  # Clear the truck's package list to reorder them

    while not_delivered:
        next_package = None
        next_address = float('inf')  # Set initial closest distance to infinity

        # Find the nearest package to the current location
        for package in not_delivered:
            distance = get_distance(get_index(truck.address), get_index(package.address))

            if distance <= next_address:
                next_address = distance
                next_package = package  # Select the package with the shortest distance

        # Update truck and package information after delivery
        truck.packages.append(next_package.package_id)
        not_delivered.remove(next_package)
        truck.mileage += next_address  # Accumulate distance traveled
        truck.address = next_package.address  # Update truck's current address
        truck.time += timedelta(hours=next_address / truck.speed)  # Update time based on speed and distance

        # Update package delivery time and departure time
        next_package.delivery_time = truck.time
        next_package.departure_time = truck.depart_time

# Execute nearest neighbor algorithm for truck routing
nearest_neighbor(truck1)  # Order packages for truck 1
nearest_neighbor(truck2)  # Order packages for truck 2

# Ensure truck 3 departs after the first two trucks have finished their deliveries
truck3.depart_time = min(truck1.time, truck2.time)
nearest_neighbor(truck3)  # Order packages for truck 3

class Main:
    '''
    Interactive user interface for the WGUPS routing program.
    Shows package details and total mileage for trucks.
    '''
    def __init__(self):
        print("Welcome to the WGUPS Routing Program")
        self.main_menu()

    def main_menu(self):
        # Main menu for user interaction
        start_input = input("Please type 'start' to begin: ").lower()
        if start_input == "start":
            self.show_menu()
        else:
            self.exit_program("Invalid entry; exiting the program.")

    def show_menu(self):
        # Display menu options for the user
        print("Enter '1' to view package details")
        print("Enter '2' to view total mileage")
        print("Enter '3' to exit the program")
        
        choice = input("Select an option: ")
        if choice == "1":
            self.view_package_details()
        elif choice == "2":
            self.view_total_mileage()
        elif choice == "3":
            self.exit_program("Goodbye!")
        else:
            print("Invalid option; please try again.")
            self.show_menu()

    def view_package_details(self):
        try:
            # Allow user to input time and select package details to view
            time_input = input("At what time do you want to view the delivery status? (e.g., 10:30 AM or 02:15 PM) ").strip()
            convert_time = datetime.strptime(time_input, "%I:%M %p").time()
            time_delta = timedelta(hours=convert_time.hour, minutes=convert_time.minute)
            
            pkg_input = input("Type 'all' to view every package or 'one' for a single package: ").lower()
            if pkg_input == "one":
                self.view_single_package(time_delta)
            elif pkg_input == "all":
                self.view_all_packages(time_delta)
            else:
                print("Invalid option; please try again.")
                self.view_package_details()
        except ValueError:
            print("Invalid time format; please use the format HH:MM AM/PM and try again.")
            self.view_package_details()

    def view_single_package(self, convert_time):
        try:
            # Allow user to view details of a single package
            single_input = input("Please choose a package ID between 1 and 40: ")
            pkg_id = int(single_input)
            pkg = pkg_hash.lookup(pkg_id)
            if pkg:
                for i, truck in enumerate(trucks, start=1):
                    if pkg_id in truck.packages:
                        print(f'Truck {i} - {pkg.update_status(convert_time)}')
            else:
                print("Package not found; please try again.")
                self.view_single_package(convert_time)
        except ValueError:
            print("Invalid package ID; please try again.")
            self.view_single_package(convert_time)

    def view_all_packages(self, convert_time):
        try:
            # Display delivery details for all packages
            for pkg_id in range(1, 41):
                pkg = pkg_hash.lookup(pkg_id)
                if pkg:
                    for i, truck in enumerate(trucks, start=1):
                        if pkg_id in truck.packages:
                            print(f'Truck {i} - {pkg.update_status(convert_time)}')
                            break  # No need to continue checking trucks once found
        except ValueError:
            self.exit_program("An error occurred; exiting the program.")

    def view_total_mileage(self):
        # Calculate and display total mileage traveled by all trucks
        total_mileage = sum(truck.mileage for truck in trucks)
        for i, truck in enumerate(trucks, start=1):
            print(f'Truck {i} traveled {truck.mileage:.2f} miles.')
        print(f'The total distance traveled by all trucks is {total_mileage:.2f} miles.')

    def exit_program(self, message):
        # Exit the program with a message
        print(message)
        exit()

# Start the program
if __name__ == "__main__":
    Main()
