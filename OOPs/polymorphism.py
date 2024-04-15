'''
The word polymorphism means having many forms. 
In programming, polymorphism means the same function name (but different signatures) 
being used for different types. 
The key difference is the data types and number of arguments used in function.

Example:
# len() being used for a string
print(len("geeks"))
 
# len() being used for a list
print(len([10, 20, 30]))

'''

# Examples of user-defined polymorphic functions: 

def add(x, y, z = 0):
    return x + y+z
 
# Driver code
print(add(2, 3))
print(add(2, 3, 4))


'''
Method Overiding
----------------------
In Python, Polymorphism lets us define methods in the child class that have the same name 
as the methods in the parent class. 
In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited 
from the parent class. 
This is particularly useful in cases where the method inherited from the parent class 
doesn’t quite fit the child class. 
In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding.  
'''

class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")

'''
Method Overloading: 
It is an example of Compile time polymorphism. 
In this, more than one method of the same class shares the same 
method name having different signatures. 
Method overloading is used to add more to the behavior of methods and 
there is no need of more than one class for method overloading.
Note: Python does not support method overloading. 
We may overload the methods but can only use the latest defined method.
'''