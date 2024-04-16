# Wrapp the function with other function.
def mydecorator(fun):
    def wrapper(*args, **kwargs):
        print("Heey Start")
        ret = fun(*args, **kwargs)
        print("Hey End")
        return ret
    return wrapper

def hello_world():
    print("Heelo world")
    
mydecorator(hello_world)()
print("------------")
@mydecorator
def hello_world_elite(person):
    print(f"Heelo world {person}")
    return person

print(hello_world_elite("Mike"))


# Logging
from time import perf_counter
from typing import Any, Callable
import logging
from math import sqrt
import functools

logger = logging.getLogger("my_app")

def with_logging_func(func: Callable[...,Any])->Callable[...,Any]:
    @functools.wraps(func)
    def wrapper(*args: Any,**kwargs: Any) -> Any:
        logging.info(f"Calling {func.__name__}")
        return_value = func(*args, **kwargs)
        logging.info(f"Finished {func.__name__}")
        return return_value
    return wrapper

def time_method(func: Callable[...,Any])-> Callable[...,Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs)->Any:
        start = perf_counter()
        return_value = func(*args, **kwargs)
        end = perf_counter()
        logging.info(f"{func.__name__} took {end-start} secs.")
        return return_value
    return wrapper


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True
        
@with_logging_func
@time_method        
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count += 1
    return count

def main()->None:
    logging.basicConfig(level=logging.INFO)
    count_prime_numbers(2000)
    
if __name__ == '__main__':
    main()