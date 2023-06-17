# sets 
SetFruits = {'apple', 'orange', 'banana'}
print ("type(setFruits) = {0} : setFruits = {1}".format(type(SetFruits), SetFruits))

# sets CANNOT be accessed using index. eg: setsFruits[1]

for item in SetFruits:
    print(item)

# add set items
SetFruits.add("grapes")
print("type(SetFruits) = {0} : setFruits = {1}".format(type(SetFruits), SetFruits))

# add elements using update function
SetFruits2 = {'papaya', 'pineapple', 'mango'}
SetFruits.update(SetFruits2)
print ("type (setFruits) = {0} : setFruits.update(setsFruit2) = {1}".format(type(SetFruits), SetFruits))


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc)

# remove item from the set
# use remove - if item does not exist, it will throw error
# use discard - - if item does not exist, it will not throw error
# clear - empty the list
# the del keyword will delete the set completely

# Join Sets 
setFlower1 = {'rose', 'lilly'}
setFlower2 = {'jasmine', 'lotus', 'lilly'}
# union
# the union() method returns a new set with all ietms from both sets
setUnion = setFlower1.union(setFlower2)
print ("type(setFlower1) = {0} : type(setFlower2) = {1} :setFlower1.update(setFlower2) = {2}".format(type(setFlower1), type(setFlower2), setUnion))

#update 
# The update() method inserts the items in setFlower2 into setFlower1
setFlower1.update(setFlower2)
print("type(setFlower1) = {0} :type(setFlower2) = {1} :setFlower1.update(setFlower2) = {2}".format(type(setFlower1), type(setFlower2), setFlower1))

# Joint two sets
setCharacters = {'a', 'b', 'c','d', 'e', 'f'}
setNumbers = {1,2,3,4,5,6,7}
# union
setUnionResult = setCharacters.union(setNumbers)
print ("SetCharacters.union(setNumbers) : {0}".format(setUnionResult))

# set with list - union
listTemp = ['one', 'two']
setMovies = {'spider man', 'behind the enimies lines'}
res = setMovies.union(listTemp)
print ("Test code : {0}".format(res))


# update 
# insert items in set1 to set 2
setCharacters.update(setNumbers)
print ("setCharacters.update(setNumbers) : {0}".format(setCharacters))


# keep only duplicates
setCompanies1 = {'google', 'amazon', 'facebook'}
setCompanies2 = {'google', 'GRT','abirami'}
setCompanies1.intersection_update(setCompanies2)
print ("SetCompanies1.insertion_update(setCompaines2) : {0}".format(setCompanies1))

# intersection
setCompanies1 = {'google', 'amazon', 'facebook'}
setCompanies2 = {'google', 'GRT', 'abirami'}
newSet = setCompanies1.intersection(setCompanies2)
print("setCompanies1.intersection(setCompines2) : {0}".format(newSet))

# Keep All, but NOT the duplicates
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.symmetric_difference_update(y)
print ("x.symmetric_difference_update(y) : {0}".format(x))

# symmetric_difference() method will return a new set
# that contains only the elements that are NOT present in both sets.
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.symmetric_difference(y)
print ("x.symmetric_difference(y) : {0}".format(z))