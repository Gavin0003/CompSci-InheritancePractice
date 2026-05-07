import vehicles

auto_mobile = vehicles.automobile('make', 'model', 'mileage', 'price')


car = vehicles.Car('Tesla', 'Y', 2864, 999999, 4)
truck = vehicles.Truck('Ford', 'F150', 2187, 9999999, 2)
suv = vehicles.SUV('', '', 4871, 99999, 5)
list = [car, truck, suv]

print()
for vehicle in list:
    print(f'The following {vehicle.get_name()} is in inventory: ')
    print(f'Make: {vehicle.get_make()}')
    print(f'Model: {vehicle.get_model()}')
    print(f'Mileage: {vehicle.get_mileage()}')
    print(f'Price: {vehicle.get_price()}')
    print(f'{vehicle.get_var()}: {vehicle.get_variable()}')
    print()
    
