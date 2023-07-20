## 2. Search Algorithms

# Binary Search: is an efficient algorithm for finding an ietm from a sorted list of items. 
# It works repeatedly dividing in half the portion of the array being searched, until the target value is found.

def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid -1 
        else:
            return mid 
    return -1

print (binary_search([1,2,3,4,5,6,7], 5)) # 4

# Hash Tables: a hash table is a DS that maps keys to values using hash function to compute an index into an array of buckets or slots, 
#              from which the desired value can be found


class HashTable:
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, data):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data # update 
                return
            index = (index +1) % self.size
        self.keys[index] = key
        self.values[index] = data

    def get(self,key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None


    def hash_function(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        return sum % self.size
    
t = HashTable()
t.put("apple", 10)
t.put("orange", 20)
t.put("banana", 30)
print (t.get("orange")) # 20