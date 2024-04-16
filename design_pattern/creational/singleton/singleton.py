'''
Intent:
----------
Singleton is a creational design pattern that lets you ensure that a class has only one instance, 
while providing a global access point to this instance.


The most common reason for this is to control access to some shared resource—for example, 
a database or a file.


Solution
---------
1)Make the default constructor private, to prevent other objects from using 
the new operator with the Singleton class.
2)Create a static creation method that acts as a constructor. 

Class --> __new__(To create object) ---> Run __init__ (As constructor)

'''

class A:
    def __new__(cls):
        print("Object is created")
    def __init__(cls):
        print("Init is called")

class B:
    def __new__(cls):
        print("Object is created")
        return super(B, cls).__new__(cls)
    def __init__(cls):
        print("Init is called")

class C:
    def __new__(cls):
        print("Object is created")
        return C.__init__(cls)
    def __init__(cls):
        print("Init is called")
    
print("__new__ without calling __init__")
A()
print("__new__ calling Parent __init__")
B()
print("__new__ calling __init__")
C()

class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            # cls._instance = super(Singleton,cls).__new__(cls)
            cls._instance = Singleton.__init__(cls)
            # logic
        return cls._instance
    

ins1 = Singleton()
ins2 = Singleton()

print(ins1 is ins2)
print(Singleton)
print(Singleton)
