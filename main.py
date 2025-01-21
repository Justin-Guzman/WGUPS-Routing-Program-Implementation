from data_loader import load_packages
from hash_table import HashTable

def get_package_info(hash_table, package_id):
    # Lookup package by ID using the hash table
    return hash_table.lookup(package_id)

def main():
    packages_csv_path = "/Users/justinguzman/Desktop/WGUPS-Routing-Program-Implementation/packages.csv"
    hash_table = HashTable()

    # Load packages into the hash table
    load_packages(packages_csv_path, hash_table)

    # Allow user to query package information by package ID
    print("Welcome to the WGUPS Routing Program!")
    
    while True:
        try:
            # Ask the user for a package ID to look up
            user_input = input("Enter a package ID to get information (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting the program.")
                break  # Exit the loop
            
            package_id = int(user_input)  # Convert to integer for lookup
            package_info = get_package_info(hash_table, package_id)

            if package_info:
                # Print package details
                print(f"Package {package_id}:")
                print(f"  Address: {package_info['address']}")
                print(f"  Deadline: {package_info['deadline']}")
                print(f"  City: {package_info['city']}")
                print(f"  Zip Code: {package_info['zip_code']}")
                print(f"  Weight: {package_info['weight']} KILO")
                print(f"  Status: {package_info['status']}")
            else:
                print(f"Package with ID {package_id} not found.")
        
        except ValueError:
            print("Invalid input. Please enter a numeric package ID.")

if __name__ == "__main__":
    main()
