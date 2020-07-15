class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_list = [None] * capacity
        self.FNV_offset_basis = 14695981039346656037
        self.FNV_prime = 1099511628211
        self.num_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """

        return len(self.hash_list)
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """

        return self.num_items / self.capacity
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash_var = self.FNV_offset_basis

        for byte_of_data in key.encode():
            temp_str = ''
            hash_var = hash_var * self.FNV_prime
            hash_set = set(str(hash_var))
            byte_set = set(str(byte_of_data))
            for val in hash_set.difference(byte_set):
                temp_str += val

            hash_var = int(temp_str)
        
        return hash_var
        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        new_hash_entry = HashTableEntry(key, value)
        previous_item = None

        if self.hash_list[self.hash_index(key)] is None:
            self.hash_list[self.hash_index(key)] = new_hash_entry
        else:
            current_item = self.hash_list[self.hash_index(key)]

            while current_item is not None:
                if current_item.key == new_hash_entry.key:
                    current_item.value = new_hash_entry.value
                    return
                else:
                    previous_item = current_item
                    current_item = current_item.next
            
            previous_item.next = new_hash_entry
            self.num_items += 1

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)



        # Your code here


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        current_item = self.hash_list[self.hash_index(key)]
        previous_item = None
        found = False

        if current_item is None:
            print('key does not exist')
        else:
            if current_item.key == key:
                current_item.value = None
            else:
                while current_item is not None:
                    if current_item.key == key:
                        previous_item.next = current_item.next
                        return
                    else:
                        previous_item = current_item
                        current_item = current_item.next

                if not found:
                    print('key does not exist')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        retrieved_value = self.hash_list[self.hash_index(key)]

        while retrieved_value is not None and retrieved_value.key != key:
            retrieved_value = retrieved_value.next

        if retrieved_value is None:
            return None
        else:
            return retrieved_value.value
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_capacity = self.get_num_slots()
        self.capacity = new_capacity
        temp_list = []

        for current_item in self.hash_list:
            temp_list.append(current_item)

        self.hash_list = [None] * self.capacity

        for current_item in temp_list:
            while current_item is not None:
                self.put(current_item.key, current_item.value)
                current_item = current_item.next


                
        # Your code here



# if __name__ == "__main__":
    # ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
