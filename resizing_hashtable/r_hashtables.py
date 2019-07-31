

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return  str(self.value)


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381

    for character in string:
        hash = ((hash << 5) + hash) + ord(character)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    new_pair = LinkedPair(key, value)
    current_pair = hash_table.storage[index]
    last_pair = None

    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = current_pair.next
    
    if last_pair == None:
        hash_table.storage[index] = new_pair
    else:
        last_pair.next = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)

    current_pair = hash_table.storage[index]
    last_pair = None
    while current_pair is not None and current_pair.key != key:
        last_pair = current_pair
        current_pair = current_pair.next

    if current_pair is None:
        print("Key", key, "does not exist")
    elif current_pair.key == key and last_pair is not None:
        last_pair.next = current_pair.next
    elif current_pair.key == key and last_pair is None:
        hash_table.storage[index] = current_pair.next
    else:
        print('oops')


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    current_pair = hash_table.storage[index]
    while current_pair is not None and current_pair.key != key:
        current_pair = current_pair.next

    if current_pair is None:
        return None
    elif current_pair.key == key:
        return current_pair.value
    else:
        print('oops')
    


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def test_print(ht):
    
    for i in range(len(ht.storage)):
        current = ht.storage[i]
        while current is not None:
            print(current)
            current = current.next

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    test_print(ht)

    hash_table_remove(ht, "line_2")

    print("---------")
    test_print(ht)
    print("---------")



    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
