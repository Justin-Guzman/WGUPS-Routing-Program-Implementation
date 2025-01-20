class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        """Generate a hash value for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]  # Create a new list if there's no collision
        else:
            # If there's a collision, append the new key-value pair to the list
            self.table[index].append((key, value))

    def search(self, key):
        """Search for a key in the hash table and return its associated value."""
        index = self._hash(key)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:
                    return item[1]  # Return the value if key matches
        return None  # Return None if the key doesn't exist

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item[0] == key:
                    del self.table[index][i]
                    return True
        return False

