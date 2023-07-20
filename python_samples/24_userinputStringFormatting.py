# 

username = input ("Enter username : ")
print ("username is: " + username)

price = 49
txt = "The price is {:.2f} dollars"
print (txt.format(price))

# index numbers 
age = 35
name = "John"
txt = "His name is {1}. {1} is {0} years old"
print (txt.format(age, name))

# name indexes
orderFormatting = "I have a {watchColour} colour Watch and {shoesColour} colour Shoes"
print (orderFormatting.format(shoeColour ="brown", watchColour = "black"))