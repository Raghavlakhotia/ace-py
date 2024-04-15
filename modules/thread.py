"""
Concurrency:
~~~~~~~~~~~~~~~~~~~
--> Fast context switching.
--> Executing multiple task at a same time but not neccesary simantaneouly.
--> Can be done with one CPU core.
P1 -> P2 -> P1 
Advantage:
- IO bound application.

Parallesim:
~~~~~~~~~~~~~~~~~~~
- Applicable only when there are multiple CPU core. 
- Not neccary multiple task but, single task can be divided in sub task and can be computed paralley,
via multiple CPU core.

"""

"""
Use to increase the compute power:
1)Multiprocessing:
More than one CPU core.
Type:
- Symmetric: SHared resource. Use same memeory and IO bus. All procesors(CPU Core) are equal power.
- Asymetric: No shared recourse. All procesors(CPU Core) are not equal power, can have master slave arch.

2)Multithreading
Multiple threasd are processed togtheer.
"""

"""
THREADS:
- A thread is a separate flow of execution. 
Python 3 implementations the different threads do not actually execute at the same time: 
they merely appear to.


"""
