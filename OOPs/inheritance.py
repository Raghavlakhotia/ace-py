'''
>> Python support multiple inhertiance.

class A:
    pass
'''


class A:
    pass

class B:
    pass

class C(A,B):
    pass

obj = C()
issubclass(C,A)
isinstance(obj, C)

'''
Method Overriding :
We can provide some specific implementation of the parent class method in our child class. 
When the parent class method is defined in the child class with some specific implementation, 
then the concept is called method overriding. 
'''
class Animal:  
    def speak(self):  
        print("speaking")  
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
        
d = Dog()  
d.speak()  


'''
Inspect Module
'''
import inspect
import numpy
import math
  

class A(object):
    pass
def fun(a):
    return 2*a
  
# use isfunction()
print(inspect.isfunction(fun))
  
# use isclass()
print(inspect.isclass(A))

# use ismodule()
print(inspect.ismodule(numpy))

# getmembers(): This method returns the member functions present in the module passed as an argument of this method.
print(inspect.getmembers(math))
