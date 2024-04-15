# Builder design will have 
#           - Builder class
#           - Director class
#           - Class for implementing all the other methods.


# Builder class: abs_builder.py 
import abc
from computer import Computer

class AbsBuilder(abc.ABC):
    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass

    @abc.abstractmethod
    def install_hard_drive(self):
        pass

    @abc.abstractmethod
    def install_video_card(self):
        pass

# Director class - director.py
class Director(object):

    def __init__(self, builder):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    def get_computer(self):
        return self._builder.get_computer()

# Method for all - computer.py
class Computer(object):

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))


# NOWW, create class for each type of paramter list. 
from abs_builder import AbsBuilder

class BudgetBoxBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Corsair'
     
    def build_mainboard(self):
        self._computer.mainboard = 'ASUS'
        self._computer.cpu = 'AMD'
        self._computer.memory = '2 X 4GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Seagate'

    def install_video_card(self):
        self._computer.video_card = 'On board'

class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Coolermaster'
     
    def build_mainboard(self):
        self._computer.mainboard = 'MSI'
        self._computer.cpu = 'Intel Core i9'
        self._computer.memory = '2 X 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'SSD'

    def install_video_card(self):
        self._computer.video_card = 'GeForce GTX'


# Main.py 
from director import Director
from mycomputer_builder import MyComputerBuilder
from budget_box_builder import BudgetBoxBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

