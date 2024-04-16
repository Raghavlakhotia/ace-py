'''
Classmethods as  alernative constructors.
'''

class Student:
    def __init__(self,name, age, subject) -> None:
        self.name = name
        self.age = age
        self.subject = subject
    
    def show(self):
        print(f"Name:{self.name}\n Age: {self.age}\n Subject: {self.subject}")
    
    @classmethod    
    def from_string(cls, string):
        name,age,subject = string.split('_')
        return cls(name,age,subject)
    
    @staticmethod
    def is_even(num):
        return True if num%2==0 else False
        
        
s1 = Student("Raghav",18,"Maths")
s2 = Student.from_string("Neha_21_chemistry")

s1.show()
s2.show()

print(Student.is_even(23))

print(Student.is_even(22))