class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0


    def __len__(self):
        return self.length


    def add_to_list(self, key, value):
        new_entry = HashTableEntry(key, value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_entry
            self.tail = new_entry
        else:
            new_entry.prev = self.tail
            self.tail.next = new_entry
            self.tail = new_entry


    def find_node(self, key):
        cur = self.head
        while cur is not None:
            if cur.key == key:
                return cur
            cur = cur.next
        return None

        
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


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
        self.storage = [None] * capacity
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.capacity)





    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

        FNV_prime = 1099511628211
        FNV_offset_basis = 14695981039346656037

        hash_index = FNV_offset_basis
        bytes_to_hash = key.encode()
        for byte in bytes_to_hash:
            hash_index = hash_index * FNV_prime
            hash_index = hash_index ^ byte
        return hash_index


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash

        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # If self.capacity[index] is none, then initiate None before adding to the list.
        # self.capacity[index] = doubly linked list
        # Then add a key and a value to the doubly linked list
    
        index = self.hash_index(key)
        if self.storage[index] is None:
        # Initiate none by setting self.capacity[index] = doubly linked list
            self.storage[index] = DoublyLinkedList()
            self.storage[index].add_to_list(key, value)
        else:
            found = self.storage[index].find_node(key)
            if found:
                found.value = value
            else:
                self.storage[index].add_to_list(key, value)

        
        
        




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        found = self.storage[index].find_node(key)
        if found is None:
            print("Warning, this key is not found.")
        else:
            self.storage[index].delete(found)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.storage[index] is None:
            return None
        else:
            found = self.storage[index].find_node(key)
            if found is None:
                return None
            else:
                return found.value
        



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
