import csv

def load_packages(file_path, hash_table):
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Ensure the column names match the headers in the CSV file
            package_id = int(row["Package ID"])  # Updated to match your CSV header
            address = row["Address"]
            city = row["City"]
            state = row["State"]
            zip_code = row["Zip"]
            deadline = row["Delivery Deadline"]  # Updated to match your CSV header
            weight = float(row["Weight KILO"]) if row["Weight KILO"] else 0  # Handle empty weight
            special_notes = row["Special Notes"]  # This might represent status or notes

            # Insert the data into the hash table
            hash_table.insert(package_id, {
                "address": address,
                "city": city,
                "state": state,
                "zip_code": zip_code,
                "deadline": deadline,
                "weight": weight,
                "status": special_notes
            })

