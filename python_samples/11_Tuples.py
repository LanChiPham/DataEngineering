# Python typles
# tuple creation

tupleFruits = ('apple', 'orange', 'cherry', 'mango')
print ("type = {0} : tupleFruits = {1}".format(type(tupleFruits), tupleFruits))
# tuple allows duplicates
tupleFruitsWithDuplicates = ('apple', 'orange', 'cherry', 'mango', 'orange')
print ("type = {0} : tupleFruitswithDuplicates = {1}".format(type(tupleFruitsWithDuplicates), tupleFruitsWithDuplicates))
# tuple length 
print ("type = {0} : len(tupleFruitsWithDuplicates) = {1} ".format(type(tupleFruitsWithDuplicates), len(tupleFruitsWithDuplicates)))

# tuple with multiple type items
tupleMultipleTypeItems = ("apple", 15, True)
print("type = {0} : tupleMultipleTypeItems = {1}".format(type(tupleMultipleTypeItems), tupleMultipleTypeItems))

# tuple constructor - two brackets with tuple()
tupleContries = tuple(("Singapore", "USA", "Australia"))
print ("type = {0} : tupleCountries = {1}".format(type(tupleContries), tupleContries))

# access tuple values 
print ("type = {0} : tupleCountries[1] = {1}".format(type(tupleContries), tupleContries[1]))

# negative indexing, index range, slicing - all works

# using if condition in tuple
if "Singapore" in tupleContries:
    print("Yes. Singapore exists in the given tuple")

#update tuple values
# change to list, update and make tuple
listCountries = list(tupleContries)
listCountries.append("England")
tupleContries = tuple(listCountries)
print("Tuple after adding \"England\" : {0}".format(tupleContries))

#unpack tuples
tupleCities = ('Chennai','Bangalore')
(ctyChennai, ctyBangalore) = tupleCities
# or ctyChennai, ctyBangalore = tupleCities
print("type = {0} : ctyChennai = {1}".format(type(ctyChennai), ctyChennai))


# packing 
tupleDuplicateCities = (ctyChennai, ctyBangalore)
print ("packing example...")
print ("Tuple packing : {0}".format(tupleDuplicateCities))

# loop 
# for - in 
# for using range(len())
# while also change be used

# Join tuples
# Add tuples
tupleAfricanCountries = (("Jamaica", "Ethiyopia"))
tupleAllCountries = tupleContries + tupleAfricanCountries
print ("All Countries tuple: {0}".format(tupleAllCountries))

# multiply 
tupleKings = ("akbar", "ashoka")
tupleKings *= 3
print ("tupleLing *= 2 : {0}".format(tupleKings))