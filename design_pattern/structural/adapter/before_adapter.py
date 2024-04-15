# WHen you have multiple object but they have some same properties and you want to print them. 

# TYPE1 - Vendor
class Vendor(object):
    def __init__(self, name, number, street):
        self._name = name
        self._number = number
        self._street = street

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def street(self):
        return self._street
        
# Type2 - Customer
class Customer(object):
    def __init__(self, name, address):
        self._name = name
        self._address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

# Main
from customer import Customer
from vendor import Vendor

MOCKCUSTOMERS = (
    Customer('Pizza Love', '33 Pepperoni Lane'),
    Customer('Happy and Green', '25 Kale St.'),
    Customer('Sweet Tooth', '42 Chocolate Ave.')
)

MOCKVENDORS = (
    Vendor('Dough Factory', 1, 'Semolina Court'),
    Vendor('Farm Produce', 14, 'Country Rd.'),
    Vendor('Cocoa World', 53, 'Tropical Blvd.')
)

def main():
    if TYPE == 'customers':
        for cust in CUSTOMERS:
            print('Name: %s; Address: %s' %
                  (cust.name, cust.address))
    elif TYPE == 'vendors':
        for vend in VENDORS:
            print('Name: %s; Address: %s %s' %
                  (vend.name, vend.number, vend.street))
    else:
        raise ValueError('Incorrect type: ' + TYPE)


