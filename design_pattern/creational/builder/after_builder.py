class Computer(object):

    def __init__(self, case, mainboard, cpu):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        
    def display(self):
        print('Custom Computer:')
        print(f'\t{"Case":>10}: {self.case}')
        print(f'\t{"Mainboard":>10}: {self.mainboard}') 
        print(f'\t{"CPU":>10}: {self.cpu}') 
        

class ComputerBuilder:
    
    def __init__(self):
        self.__case = None
        self.__mainboard = None
        self.__cpu = None

    @staticmethod
    def get_computer():
        return Computer(ComputerBuilder.__case,
                        ComputerBuilder.__mainboard,
                        ComputerBuilder.__cpu)
    
    @classmethod
    def set_case(cls, value):
        cls.__case = value
        return cls
    
    @classmethod
    def set_mainboard(cls, value):
        cls.__mainboard = value
        return cls
    
    @classmethod
    def set_cpu(cls, value):
        cls.__cpu = value
        return cls


computer2 = ComputerBuilder().set_case("Coolermaster").set_mainboard('MSI').set_cpu(2).get_computer()
computer2.display()


# ---------------More Optimized version
from abc import ABC, abstractmethod

class IBuilder(ABC):

    @abstractmethod
    def set_case(self, value):
        pass

    @abstractmethod
    def set_mainboard(self, value):
        pass

    @abstractmethod
    def set_cpu(self, value):
        pass

    @abstractmethod
    def get_computer(self):
        pass


class Computer(object):

    def __init__(self, case, mainboard, cpu):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        
    def display(self):
        print('Custom Computer:')
        print(f'\t{"Case":>10}: {self.case}')
        print(f'\t{"Mainboard":>10}: {self.mainboard}') 
        print(f'\t{"CPU":>10}: {self.cpu}') 
        

class ComputerBuilder(IBuilder):
    
    def __init__(self):
        self.__case = None
        self.__mainboard = None
        self.__cpu = None

    def set_case(self, value):
        self.__case = value
        return self
    
    def set_mainboard(self, value):
        self.__mainboard = value
        return self
    
    def set_cpu(self, value):
        self.__cpu = value
        return self

    def get_computer(self):
        return Computer(self.__case,
                        self.__mainboard,
                        self.__cpu)


# Example usage
computer_builder = ComputerBuilder()
computer2 = computer_builder.set_case("Coolermaster").set_mainboard('MSI').set_cpu(2).get_computer()
computer2.display()
