from data_loader import load_packages
from hash_table import HashTable

def main():
    packages_csv_path = "/Users/justinguzman/Desktop/WGUPS-Routing-Program-Implementation/packages.csv"
    hash_table = HashTable()

    load_packages(packages_csv_path, hash_table)  # Pass the full path here

    # Print hash table contents for debugging
    for package_id in range(1, 41):  # Adjust range if you have more/less packages
        result = hash_table.search(package_id)
        if result:
            print(f"Package {package_id}: {result}")
        else:
            print(f"Package {package_id}: Not found")

if __name__ == "__main__":
    main()


