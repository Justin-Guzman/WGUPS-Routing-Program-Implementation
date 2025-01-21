class HashTable:
    def __init__(self, size=40):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, package_id, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status):
        index = self.hash_function(package_id)
        self.table[index] = {
            'package_id': package_id,
            'address': delivery_address,
            'deadline': delivery_deadline,
            'city': delivery_city,
            'zip_code': delivery_zip_code,
            'weight': package_weight,
            'status': delivery_status
        }

    def lookup(self, package_id):
        index = self.hash_function(package_id)
        package = self.table[index]
        
        # Ensure the package exists and matches the requested ID
        if package and package['package_id'] == package_id:
            return package
        else:
            return None
