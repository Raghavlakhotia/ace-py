# There are two type of adpater: Object and class adpater. (Object is better)
# Adpater pattern is also know as Wrapper pattern.


# Adapter class
import abc

class AbsAdapter(abc.ABC):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    @property
    def adaptee(self):
        return self._adaptee

    @abc.abstractproperty
    def name(self):
        pass

    @abc.abstractproperty
    def address(self):
        pass

# Vendor adpater
from abs_adapter import AbsAdapter

class VendAdapter(AbsAdapter):
    @property
    def name(self):
        return self.adaptee.name

    @property
    def address(self):
        return '{} {}'.format(
            self.adaptee.number,
            self.adaptee.street
        )
        
# Customer adpater
from abs_adapter import AbsAdapter

class CustAdapter(AbsAdapter):
    def name(self):
        return self._adaptee.name

    def address(self):
        return self._adaptee.address
        
# main

from customer import Customer
from vendor import Vendor

from mock_vendors import MOCKVENDORS
CUSTOMERS = MOCKVENDORS

MOCKCUSTOMERS = (
    Customer('Pizza Love', '33 Pepperoni Lane'),
    Customer('Happy and Green', '25 Kale St.'),
    Customer('Sweet Tooth', '42 Chocolate Ave.')
)

MOCKVENDORS = (
    VendAdapter(Vendor('Dough Factory', 1, 'Semolina Court')),
    VendAdapter(Vendor('Farm Produce', 14, 'Country Rd.')),
    VendAdapter(Vendor('Cocoa World', 53, 'Tropical Blvd.'))
)

def main():
    for cust in CUSTOMERS:
        print('Name: %s; Address: %s' %
              (cust.name, cust.address))

if __name__ == '__main__':
    main()


