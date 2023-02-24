# listof available cars and their prices
cars = {
        'McLaren': 341000,
        'Porsche': 67500,
        'Audi TT': 51200,
        'Bugatti': 1900628,
        'Audi AB': 87985,
        'Lamborghini Aventador': 557945,
        'Ferrari': 931500,
        'Lexus': 68000,
        'G-Wagon': 139800,
        'SUV': 57203,
        'Rols Royce Phanthom': 470000,
        'Lamborghini': 557945,
        'Infiniti G': 29785,
        'Range Rover': 107520,
        'BMW': 87800,
        'Bentley': 200726,
        'BMW 7': 86800,
        'BMW Alphina XB7': 141300, 
        'Tesla': 53900,
        'Audi': 58558,
        'Bentley Bentaya': 192000,
        'Genesis': 49500,
        'Toyota Century': 179000,
        'BMW i8':143500,
        'Ford Series': 58395,
        'Toyota Camry XSE': 31245,
        'Lamborghini Urus': 138573,
        'Ford': 83241,
        'Lexus LS': 78095,
        'Mercedes Benz': 90000,
        }
# get user input for car name
car_name = input('Enter a car_name:')
# check if car name is in the list of available cars
if car_name in cars:
    print('Yes')
    #if car name is present, get its price
    car_price = cars[car_name]
    print(f'The price of {car_name} is $ {car_price}')
else:
    # if car name is not present, inform the user
    print(f'Sorry, {car_name} is not available.')
    