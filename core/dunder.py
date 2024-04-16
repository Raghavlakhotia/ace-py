'''
Python Magic methods are the methods starting and ending with double underscores ‘__’. 
They are defined by built-in classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.

__init__
__new__

__repr__
__str__


'''

class Student:
    def __init__(self,
                 name,
                 age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Student(name = {self.name}, age = {self.age})"
        

s = Student("Raghav",23)
print(s)
print(s.__repr__())


    
