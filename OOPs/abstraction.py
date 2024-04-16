'''
The main goal of the abstract base class is to provide a standardized way to test 
whether an object adheres to a given specification. 
It can also prevent any attempt to instantiate a subclass that doesn’t override 
a particular method in the superclass. And finally, using an abstract class, 
a class can derive identity from another class without any object inheritance.

>> you cant create object from abstract class.
>> ABstraction is not directly supported in python irectly but 
we can use abc(abstract base class) module.

'''
from abc import ABC, abstractmethod, abstractproperty

class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        raise NotImplementedError("This should be implemneted")
    
    @abstractproperty
    def max_speed(self):
        pass

class car(Vehicle):
    def wheels(self):
        print("4 wheels")
    
    def max_speed(self):
        return "200 Km/Hr"


def main():
    obj = car()
    obj.wheels()
    print(obj.max_speed)


if __name__=='__main__':
    main()
