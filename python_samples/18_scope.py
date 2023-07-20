# local scope
# variable declared inside the function can't be accessed outside of it 

def localFunction():
    localVariable = 2000
    print (localVariable)

localFunction()
# local variable can be accessed from a function within a function
def outerLocalFunction():
    outerLocalFunction = 100
    def innerLocationFunction():
        print (outerLocalFunction)

    innerLocationFunction()
outerLocalFunction()


# global scope y
# created outside of function can be asserted inside the function as well

x = 100
def myFunction():
    print(f"local function call. x : ${x}")

myFunction()
print(x)


# if we modify the same variable name, python will treat both are different variables. 

y = 150
def myFunction():
    global y
    y = 200
    print (f"local function. y = {y}")

print (f"global print1: {y}")
myFunction()
print (f"global print2 : {y}")