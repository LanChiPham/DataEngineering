# string
x = "Hello World"
print ("type(x) = {0} : x = {1}".format(type(x),x))

# integer 
x = 20
print ("type(x) = {0} : x = {1}".format(type(x),x))

# float 
x = 20.5
print ("type(x) = {0} : x = {1}".format(type(x),x))

# complex 
x= 1j
print ("type(x) = {0} : x = {1}".format(type(x),x))

# boolean
x = True
print ("type(x) = {0} : x = {1}".format(type(x),x))
x = False
print ("type(x) = {0} : x = {1}".format(type(x),x))

# byte type
# byte() function returns a bytes object that CANNOT be modified
# it converts objects into bytes object
# or create empty byte object of the specified size
x = bytes(5)
print ("type(x) = {0} : x = {1}".format(type(x),x))
x = b"Hello"
print ("type(x) = {0} : x = {1}".format(type(x),x))

# x[1] = 5 # gives error as its immutable 
# to_bytes - return an array of bytes representing an integer
x = (1234).to_bytes(10,byteorder = 'big')
print ("type(x) = {0} : x = {1}".format(type(x),x))

# bytearray
x = bytearray(5)
x[0], x[1], x[2], x[3], x[4] = 1,2,3,4,5
print ("type(x) = {0} : x = {1}".format(type(x),x))

# using memoryview function
# return memory view of the objects
# allows direct read and write access
# to an object's byte-orriented data without needing a copy it first
x = memoryview(bytes(5))
print ("type(x) = {0} : x = {1}".format(type(x),x))
x = memoryview(bytearray('xyz', 'utf-8'))
print(x[0])
print (bytes(x[0:2]))



# BASIC DATASTRUCTURES
#1. List
x = ["apple", "banana", "cherry"]
print ("type(x) = {0} : x = {1}".format(type(x),x))

# 2. tuples
x = ("apple", "banana", "cherry")
print ("type(x) = {0} : x = {1}".format(type(x),x))

# range
x = range(6)
print ("type(x) = {0} : x = {1}".format(type(x),x))
for i in x:
    print (i)

# dict
x = {"name":"Peter", "age":20}
print ("type(x) = {0} : x = {1}".format(type(x),x))

# set
x={"Sinagapore", "Australia", "USA"}
print ("type(x) = {0} : x = {1}".format(type(x),x))

# frozenset
# frozenset is the same as set except the frozensets are immutable
x = frozenset({"Singapore", "Australia", "USA"})
print ("type(x) = {0} : x = {1}".format(type(x),x))
