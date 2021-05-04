class Calculate:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def multiply(self):
        
        return self.val1*self.val2
    
    def add(self):
        
        return self.val1 + self.val2
        
    def misc(self, a, b):
        
        return self.val1*7/(self.val2*3) + a*(b**3)

class empty: # if we want to create a class that has no use  
    pass

obj = Calculate(10, 20)
obj1 = Calculate(3, 7)
obj2 = Calculate(5, 6)

obj.val1 = 20
obj1.val1 = 9

# delete a property of object
del obj2.val2

obj2.val2 = 5

# delete object
del obj2

# inheritance

# child class
class Calc(Calculate): # now this class will inherit all the properties of 'Calculate' class
    pass # we will use pass key when we dont want to add any more properties to the class

obj3 = Calc(5, 5)

# here i added an additional property to the class after inheriting some from 'Calculate'
class Calc2(Calculate):
    def power(self):
        
        return self.val1**self.val2

obj4 = Calc2(2, 9)

# if we add an __init__ function to the child class, the properties of parent class will be overwritten 
class Calc3(Calculate):
    def __init__(self, val3, val4, val5):
        self.val3 = val3
        self.val4 = val4
        self.val5 = val5
    
    def misc2(self):
        
        return self.val3**self.val4 + self.val4/self.val5


obj5 = Calc3(5, 5, 5)

# 
class Calc4(Calculate):
    def __init__(self, val3, val4):
        Calculate.__init__(self, val3, val4)
        self.val3 = val3
        self.val4 = val4
    
    def misc3(self):
        return self.val3*self.val4

obj6 = Calc4(2,2)


print(obj.multiply())
print(obj1.misc(2, 3))
#print(obj2.add()) # throws an error since we deleted the object 'obj2'
print(obj3.add()) # gives an output of addition of two arguments given to 'obj3'
print(obj4.power())
print(obj5.misc2())
print(obj6.misc3())




