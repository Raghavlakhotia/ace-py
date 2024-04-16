# Type hinting is only for documenation, You can bypass it. (you can run mypy <>.py to catch all these issue)
a:int = "Hello world"
print(a)

# More example
my_list: list[int] = [1,2,3]
my_dict: dict[str,int] = {"hey":1}

#For void  def increase(salary: str) -> None:
def increase(salary: str) -> int:
    return int(salary)*1.10

print(increase("200"))

# More better way for complex data structure.
tcp_dict = dict[str, list[str]]

google_port: tcp_dict = {
    "Main server" : ["1.1.1.1",
                     "2.2.3.4"]
}

from typing import Any, Sequence, Callable, Union, Optional

def fun(n: Any)->Any:
    return n*2

print(fun(1))
print(fun("1"))
print(fun([1,2]))

# Sequence is just a list of any type. list[Any]
# def fun1(s: Sequence):
#     for x in s:
#         print(x)

# print(fun1([1,2]))
# print(fun1(["1","2","3"]))

def fun2(f: Callable):
    print(f(1))

fun2(fun)    

def top_up(seat: str,
           popcorn: Optional[bool]=False)-> None:
    print(f"Seat: {seat}, Popcorn: {popcorn}")

top_up("A2")
top_up("A2",True)
top_up("A2",False)


def mmm(s: str | int) -> bool | int:
    pass
