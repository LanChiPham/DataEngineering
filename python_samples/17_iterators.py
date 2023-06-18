# iterator example - Repetitive execution of the same block of code over and over. 

fruitsTuple = ("apple", "orange", "cherry")
itFruit = iter(fruitsTuple)

print (next(itFruit))
print (next(itFruit))
print (next(itFruit))
# print (next(itFruit)) - will throw StopIteration exception


myString = "banana"
itChar = iter(myString)

print (next(itChar))
print (next(itChar))
print (next(itChar))
print (next(itChar))
print (next(itChar))
print (next(itChar))
# print (next(itChar)) - will throw StopIteration exception 


# creating iterator
# use __iter__() and __next__() function 
class FiveNumbers:
    def __iter__(self):
        self.n = 1 
        return self
    
    def __next__(self):
        if self.n <= 5:
            number = self.n
            self.n += 1
            return number
        
        else:
            raise StopIteration
        

objNumber = FiveNumbers()
iterNumber = iter(objNumber)
print ("Iterate class object...")
print (next(iterNumber))
print (next(iterNumber))
print (next(iterNumber))
print (next(iterNumber))
print (next(iterNumber))

