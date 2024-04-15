'''
# Simple Factory
-------------

def get_car(carname):
    if carname == 'Merc':
        return Merc()
    elif carname == 'Audi':
        return Audi()
    elif carname == 'Redbull':
        return Redbull()
    else:
        return nullCar(carname)
    
for car in 'Merc','Audi','Redbull':
    car = get_car(car)
    car.start()
'''
import abc
class AbsAuto(abc.ABC):
    """
    Abstract class
    """
    @abc.abstractmethod
    def start(self):
        pass

class Merc(AbsAuto):
    def start(self):
        print("Merc starting..")
        
class Audi(AbsAuto):
    def start(self):
        print("Audi starting..")

class Redbull(AbsAuto):
    def start(self):
        print("Redbull starting..")
    
class NullCar(AbsAuto):
    def __init__(self, carname):
        self._carname = carname
        
    def start(self):
        print(f"Unknown car : {self._carname}")
        
from inspect import getmembers, isclass, isabstract

class AutoFactory(object):
    autos = {}
    def __init__(self):
        self.load_autos()
    
    def load_autos(self):
        classes = getmembers(AutoFactory.autos,
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsAuto):
                self.autos.update([name, _type])

    def create_instance(self, carname):
        if carname is self.autos:
            return self.autos[carname]()
        else:
            return NullCar(carname)

def main():
    factory = AutoFactory()
    for car in 'Merc','Audi','Redbull','BMW':
        car = factory.create_instance(car)
        car.start()

if __name__=='__main__':
    main()

