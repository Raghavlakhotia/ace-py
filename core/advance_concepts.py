# Zip function

countries = ["Ecuador", "Perú", "Colombia", "USA", "Chile"]
capitals = ["Quito", "Lima", "Bogotá", "Washington DC", "Santiago"]
cities = ["Guayaquil", "Trujillo", "Medellín", "New York", "Valparaíso"]
countries_and_capitals = zip(countries, capitals, cities)

# Enumerate
for index, element in enumerate(fruits):
    pass

# Counters
from collections import Counter
fruits = ["apple", "apple", "apple", "watermelon", "grapes", "grapes"]
counts = Counter(fruits)
# >> Counter({'apple': 3, 'watermelon': 1, 'grapes': 2})
counts.most_common(1)
counts["apples"]
dict(counts.items())

# Map (map is not iterable so convert to list.) 
# map(function,list)

def double(n:int)->int:
    return n*2
arr = [1,2,3,4]
c = map(double,arr)
cc = list(map)
d = list(map(lambda x:x*2, arr))

# Reduce
# reduce(function, list)
from functools import reduce  
def ad(a,b):
    return a+b
s = reduce(ad,arr)
ss = reduce(lambda a,b:a+b,arr)

# Filter 
def is_even(x):
    return True if x%2==0 else False

# WAY 1:
# ~~~~
m = list(filter(lambda x: x%2==0), numbers)

# WAY 2:
# ~~~~
n = list(filter(is_even,numbers))



import operator
# 1)Summing up a list of numbers
total = reduce(operator.add, numbers)
# 2) Product of a list of numbers
total = reduce(operator.mul, numbers)
# 3) Concatenating strings
strings = ['Hello', ' ', 'World']
sentence = reduce(lambda x, y: x + y, strings)

# Reverse a String (S[start:stop:step])
s[::-1]

# sort and sorted()
# sort() --->  used to sort a list in place.
# sorted() ---> used to return a new sorted list from the elements of any iterable.
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

my_list.sort()
# Sort the list based on the remainder of each element when divided by 3
my_list.sort(key=lambda x: x%3)

new_sorted_list = sorted(my_list, key=lambda x: x%3)

# my default --> Accesdcing(Increasing) 
# reverse=True ---> Desecnding(Decresing)
sorted(key =..., reverse=True)
my_list.sort(key =..., reverse=True)


# Increse teh recursion limit.
import sys
new_limit = 10000  # Set the new recursion limit
sys.setrecursionlimit(new_limit)

