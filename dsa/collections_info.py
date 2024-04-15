# Counters
# -------------------------------------------------------
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# Updates
coun = Counter()
coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)
coun.update([1, 2, 4])
print(coun)

# Subtract 
c1 = Counter(A=4,  B=3, C=10)
c2 = Counter(A=10, B=3, C=4)
 
c1.subtract(c2)
print(c1)


# handle
my_counter = Counter('abracadabra')
print(my_counter.keys())
print(my_counter.values())
print(my_counter.items())


# Ordered Dict: dictionary subclass that remembers the order that keys were first inserted
# -------------------------------------------------------

from collections import OrderedDict

vanilla_dict = {}
ord_dict = OrderedDict()
vanilla_dict['a']=1
vanilla_dict['b']=3
vanilla_dict['d']=2
vanilla_dict['e']=4
ord_dict['a']=1
ord_dict['b']=3
ord_dict['e']=4
ord_dict['d']=2
print(f"Vanilla Dict :{vanilla_dict}")
print(f"Ordered dict {ord_dict}")


# Named Tuple

from collections import namedtuple

Student = namedtuple('Student',['name','age'])
s1 = Student("Raghav", 18)


# Deque (Doubly Ended Queue)
# Deque is preferred over a list in the cases where we need quicker append 
# and pop operations from both the ends of the container, 
# as deque provides an O(1) time complexity for append and pop operations 
# as compared to a list that provides O(n) time complexity.

from collections import deque

q = deque(['name','age','class'])
print("deque: ", de)
de.append(4)
print("\nThe deque after appending at right is : ")
print(de)
de.appendleft(6)
 
# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

# pop() popleft() len() de[0] de[-1] reverse()
 
# Heap: Heap data structure is mainly used to represent a priority queue. 
# -------------------------------------------

#  The property of this data structure in Python is that each time the 
#  smallest heap element is popped(min-heap). 
#  Whenever elements are pushed or popped, heap structure is maintained. 
#  The heap[0] element also returns the smallest element each time. 

import heapq
l = [5,9,0,1,3,19,54,87,92,34,44]
heapq.heapify(l)

# printing created heap
print ("The created heap is : ",(list(li)))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))
 
# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))

# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))
 
# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))
