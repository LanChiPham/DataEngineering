# List 
# use square bracket to create list
listNumbers = ["One", "two", "Three", "Four",1]

# print list
print ("print list numbers: {0}".format(listNumbers))
print ("print list using for loop:")
for item in listNumbers:
    print (item)

# access using index
print ('Access using index : ')
print (listNumbers[1])

# print length
print ("Length of the list : {0}".format(listNumbers))
# type 
print("Type of the list: {0}".format(type(listNumbers)))
# use list() constructor - double round bracket
listCopy = list(("Apple", "Orange"))
print("type : {0}, elements : {1}".format(type(listCopy), listCopy ))


# slicing can be applied 
print("Listnumbers[-1]: {0}".format(listNumbers[-1]))
print ("ListNumbers[-3:-1] : {0}".format(listNumbers[-3:-1]))


# check if item exist
if "Two" in listNumbers:
    print ("Yes. Two exists in the given list")

# Change list item
listNumbers[1] = "Two Overwrite"
print ("Two has been overwritten : {0}".format(listNumbers))
listNumbers[2:4] = ["Three Overwrite", "Four Overwrite"]
print ("Three and Four have been overwriten: {0}".format(listNumbers))
# insert items 
listNumbers.insert(1,"Two")
print ("Two inserted : {0}".format(listNumbers))


#new list
listFruits = ["apple", "orange", "mango","cherry"]
listFlowers = ["rose", "jasmine", "lilly"]

# extend list
print ("extend : {0}".format(listFruits))

# Add list items

# remove list items 
print ("original list: {0}".format(listFruits))
listFruits.remove("apple") # remove specified item
print ("ListFruits.remove(\"apple\") : {0}".format(listFruits))
listFruits.pop() # remove the item from the last index 
print ("listFruits.pop() : {0}".format(listFruits))
listFruits.pop(1) # remove item from the 1st index
print ("ListFruits.pop(1) : {0}".format(listFruits))
del listFruits[0] # delete all the items
# print ('del listFruits : {0}".format(listFruits)) - list is fully deleted
# create new list from the existing one
listFruits = ["apple", "orange", "mango", "cherry"]
# clear list
listFruits.clear()

# Loop list
listFruits = ["apple", "orange", "mango", "chery"]
print ("loop the list")
for item in listFruits:
    print(item)

print ("loop the list using index")
for index in range(len(listFruits)):
    print (listFruits[index])
    index +=1 

print ("Loop the list using list comprehension approach")
[print(item) for item in listFruits]

# list comprehension
listNew = []
for item in listFruits:
    if "a" in item:
        listNew.append(item)

print ("New list WITHOUT using list comprehension : {0}".format(listNew))

# with if 
listNew = [item for item in listFruits if "a" in item]
print ("New list using list comprehension (with if) : {0}".format(listNew))

# without if 
listNew = [item for item in listFruits]
print ("New list using list comprehension (without if): {0}".format(listNew))

# with if else (move the if condition left side of the for loop)
listNew = [item if 'a' in item else "Durian" for item in listFruits]
print ("New list using list comprehension (with if else) : {0}".format(listNew))

# Sort list 
# made all the list content to lower case 
listNew = [item.lower() for item in listFruits]
print ("Sort list example - ascending")
listNew.sort()
print (listNew)
print("Sort list example - decending")
listNew.sort(reverse=True)
print (listNew)


# sort using custom sort function
def modify_item(item):
    newItem = "A" + item + "Z"
    return newItem

print ("custom function sort...")
listFruits.sort(key = modify_item)
print(listFruits)

# copy list
# approach 1: use copy method 
listFruits2= listFruits.copy()
print ("List copy example : {0}".format(listFruits2))

# approach 2: use list() method
listFruits2 = list(listFruits)
print("list copy example: {0}".format(listFruits2))

# Join list - join two list
# 1. Use + operator
# 2. Use append function
# 3. use extend method

# List method
