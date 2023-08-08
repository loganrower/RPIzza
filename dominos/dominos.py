from pizzapi.customer import Customer
from pizzapi.address import Address

customer = Customer('Sebastian', 'Hardin', 'sebastian.hardin@gmail.com', '9712850873')
print(vars(customer))

address = Address('806 SW Western Blvd', 'Corvallis', 'OR', '97333')
print(vars(address))

store = address.closest_store()
print(vars(store))

menu = store.get_menu()
menu.display()
