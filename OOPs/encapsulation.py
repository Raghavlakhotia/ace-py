'''
Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit. 
In encapsulation, the variables of a class will be hidden from other classes, 
and can be accessed only through the methods of their current class.

Let us see the access modifiers in Python to understand the concept of Encapsulation and data hiding −

public -> accessible from inside or outside the class.
private(__variable) -> accessible from inside the class.
protected(__variable) -> accessible from inside the class and its sub-class.

'''

class Student:
    
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self._gender = gender
        
    # This is recommed to get private variables.
    @property
    def name(self):
        return self.__name
    
    def gender(self):
        return self._gender
    
def main():
    s1 = Student("Raghav",20,"Male")
    print(s1.__name)
    print(s1.name)
    print(s1.gender())
    print(s1._gender)
    print(s1.__name)
    
if __name__=="__main__":
    main()
    