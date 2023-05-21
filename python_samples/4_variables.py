# variable example

x = 1
y = "John"
print (x)
print (y)


# casting
x = str(3) #x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print (x)
print (y)
print (z)

#get type
print (type(x)) # str 
print (type(y)) # int
print (type(z)) # float

# single or double quotes 
name = "Chloe"
# same as 
name = 'Chloe'

# case sentive  - below will create two variables 
age = 10 
Age = 25

# Many values to multiple variables
print ("Many values to multiple variables")
x = y = z = "Orange", "Apple", "Pear "
print ("x = " + x + " y = " + y + " z = " + z)

# same value to multiple variable
print ("Same value to multiple variables")
x = y = z = "same value"
print ("x = " + x + " y = " + y + " z = " + z)

# unpack collections
print ("unpack collections")
fruits = ["Apple", "Orange", "Mango"]

a,b,c = fruits 
print ( "a = " + a + "  : b = " + b + "  :  c = " + c )


# output variables example 
print ("Output variables example")
print ("Value of a is: " + a )
print ("a + b = " + a + b) # same types of variables can be added
# another one is using format function
# however, STR and INT cannot be added.

# global variables
g_var = "global initial values"
def sample_fun():
    print(g_var)


def sameple_fun2():
    global g_var2
    g_var2 = "global variable value 2"

sample_fun()
sameple_fun2()

print ("global variable example")
print (g_var)
print (g_var2)


