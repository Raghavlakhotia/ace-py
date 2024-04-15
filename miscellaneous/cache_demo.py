from functools import wraps
from time import perf_counter
import sys

def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args)+str(kwargs)
        
        if key not in cache:
            cache[key] = func(*args,**kwargs)
        return cache[key]
    return wrapper

@memoize        
def fib(n:int)->int:
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

def main()->None:
    start = perf_counter()
    fib(25)
    end = perf_counter()
    print(f"Total time taken is {end-start} sec.")
    
if __name__ == "__main__":
    main()