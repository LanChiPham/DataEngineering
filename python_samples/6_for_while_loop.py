# while loop
# 1. simple while loop
print ('1. simple while loop')
count = 0
while count < 5:
    count +=1 
    print (count)

# while with break
print ("2.while with break")
count = 0
while count < 5:
    count +=1 
    print (count)
    if count == 2:
        break;

# while with continue 
print ("3. While with continue")
count = 0
while count < 5:
    count +=1 
    if count == 2:
        continue; # skipping printing 2 
    print (count)

# while with else
print ("4. While with else")
count = 6 
while count < 5:
    count +=1
    if count == 2:
        continue; # skip printing 2
    print(count)
else:
    print("while loop is not executed...else block executed")

# for loops:
print ("1. Simple for loop")
fruits = ["apple", "banana", "cherry"]
#1. simple for loop
for fruit in fruits:
    print (fruit)

# for loop - else:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "apple":
        continue;
    print(fruit)
else:
    print("for loop is not executed...else block executed")


# for loop - break 
# for loop - continue
# for loop - with pass

# range function
print ("for loop with range function")
for x in range(5): # print 0 to 4
    print(x)