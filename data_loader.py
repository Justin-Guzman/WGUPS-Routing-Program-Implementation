import csv

def load_packages(packages_csv_path, hash_table):
    # Open and read the CSV file
    with open(packages_csv_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            package_id = int(row[0])
            delivery_address = row[1]
            delivery_deadline = row[5]
            delivery_city = row[2]
            delivery_zip_code = row[4]
            package_weight = float(row[6])

           

            delivery_status = row[6]  # 'At the hub', 'En route', or 'Delivered'

            # Pass all individual components as arguments to insert into hash table
            hash_table.insert(package_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status)
