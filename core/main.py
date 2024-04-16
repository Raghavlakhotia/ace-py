# List comprehension
power_of_two = [2 ** x for x in range(20) if x % 5 == 0]
print(power_of_two)

words = ['automobile', 'car', 'anger']
words = [word.upper() if word.startswith('a') else word for word in words]
print(words)

# Map
numbers = [1,3,5,6,8]
def square(x):
    return x ** 2
l = map(square, numbers)
print(list(l))

# Ternary operator
age = 12
adult = True if age>=18 else False

# Lambda (Single line function) 

mysquare = lambda x,y: x **2 + y
print(mysquare(5,2))

mylabfunc = lambda *args: sum(args)
print(mylabfunc(1,2,3,4,5))



# Return a function
def myfunc(n):
    return lambda x: x*n
ten_multiplier = myfunc(10)
print(ten_multiplier(54))

# Enumeration (index and values)
mynames = ['mark', 'luis', 'carry']
for index, name in enumerate(mynames):
    print(index, name)
print(list(enumerate(mynames)))
print(dict(enumerate(mynames)))

# any() and all() : List of booleon 
# any : if alleast one value in true then true.
# all : if all values are true
g = [True, False, True]
print(any(g))
print(all(g))

# Reverse list
words = words[::-1]

# join
d = ",".join(words)

# doc 
print(square.__doc__)

# Zip function
name = ['Mark', 'srp', 'mohan']
age = [12,54,67]
for name, age in zip(name,age):
    print(name,age)
zipped = [('Mike',50),('Bob',23)]
names, age = zip(*zipped)
data = sorted(zip(age,name))
mydict = dict(zip(name,age))

# Swap
a= 10
b = 20 
a,b = a,b
# XOR
a = a^b
b = b^a
a = a^b
    
# Merge dict
dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'd':4}

dict3 = {**dict1, **dict2}
dict3 = dict1 | dict2 
# | is union


# *args (non-keyword arguments)
# **kwargs (keyword arguments)
def add(*args):
    print(args)
    return sum(args)
add(1,4,6,8,3)

def print_fruits(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
print_fruits(apple=60, watermelon=100, grapes=200)

