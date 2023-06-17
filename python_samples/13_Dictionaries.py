# simple dictionary 

dictAddress = {'name': 'TomBrenner', 'address' : 'hilsbro usa', 'age' : 45}
print ("print the whole dictionary : {0}".format(dictAddress))
print ("print dictionary item: {0}".format(dictAddress['name']))


# access the values 
# approach 1 - call DOES throw if the key does not exist
print('dictAddress[\'name\'] : {0}'.format(dictAddress['name']))
# approach 2 - call does not throw if the key does not exist
print ('dictAddress.get(\'name\') : {0}'.format(dictAddress.get('name')))

# print keys 
print ('dictAddress.keys() : {0}'.format(dictAddress.keys()))

# print values 
print ('dictAddress.values() : {0}'.format(dictAddress.values()))

# update value 
dictAddress['name'] = 'dan dan'
dictAddress['weight'] = 50
print('Print Values after change : {0}'.format(dictAddress.values()))

# return the key value pair as list
print('dictAddress.items() : {0}'.format(dictAddress.items()))

if 'name' in dictAddress:
    print('name key exists....')

# update values
# approach 1 :use []
# approach 2: call update method with key value pair
dictAddress.update({'name' : 'Sanjay Ramasamy'})
print('print values after update: {0}'.format(dictAddress.values()))

# add new item
# either use [] or update with new key 

# remove items from dictionary 
# use pop - remove items with the specific key
# popitem() method removes the last inserted item
# the del keyword removes the item with the specified key name 
del dictAddress['age']
# del dictAddress will delete the dictionary itself, later wec cannot use it.
# clear with empties the dictionary

# loop dictionaries 
# print all key names in the dictionary, one by one:
print ("Print all keys one by one :")
for key in dictAddress:
    print (key)

print('print all values:')
for key in dictAddress:
    print(dictAddress[key])
print('---------------------------')
for value in dictAddress.values():
    print (value)
# looping key value pair
for x, y in dictAddress.items():
    print (x,y)

# copy dictionary
#1. use .copy method 
#2. dict() constructor

# nested dictionaries
my_family = {
    "child1" :{
        "name" :'Emil',
        "year" : 2004
    },
    "child2" :{
        "name" : "Hung",
        "year" : 2011
    },
    "child3" : {
        "name" : "Chi",
        "year" : 2010
    }
}

# Nested dictionaries
child1 = {
    "name" :'Emil',
    "year" : 2004
}
child2 = {
    "name" : "Hung",
    "year" : 2011
}
child3 = {
    "name" : "Chi",
    "year" : 2010
}

my_family = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}