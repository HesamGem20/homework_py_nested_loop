#Task 1:
#1
def sum_matrix(matrix):
    total = 0
    for row in matrix:
        for num in row:
            total += num
    return total

matrix = [
    [1, 1, 1, 2, 1],
    [2, 3, 2, 2, 2],
    [3, 3, 2, 3, 3],
    [4, 4, 4, 3, 4]
]
result = sum_matrix(matrix)
print(result)


#Task 2:

def check_passenger_qty(cars):
    for car in cars:
        if len(car["passengers"]) > car["passengerQty"]:
            print(f"The {car['type']} car has too many passengers")

cars = [
    {
        "price": 1549,
        "passengerQty": 4,
        "currency": "EUR",
        "type": "Kia",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 1954,
        "passengerQty": 5,
        "currency": "EUR",
        "type": "Suzuki",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 5,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 2,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
    {
        "price": 9542,
        "passengerQty": 4,
        "currency": "USD",
        "type": "Ford",
        "transmission": "automatic",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
]

check_passenger_qty(cars)


#Task 3:


def convert_currency(cars, exchange_rate):
    for car in cars:
        if car["currency"] == "EUR":
            car["price"] *= exchange_rate

def display_car_prices(cars):
    for car in cars:
        print(f"{car['type']} - Price: {car['price']} {car['currency']}")

exchange_rate = 1.2  # Assuming 1 EUR = 1.2 USD
convert_currency(cars, exchange_rate)
display_car_prices(cars)


#Task 4:


persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

for person in persons:
    for restaurant in restaurants:
        print(f"{person} eats {restaurant}")


#Task 5:


def add_sum_to_list(lst):
    for sublist in lst:
        sublist.append(sum(sublist[:2]))

my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]
add_sum_to_list(my_list)
print(my_list)


#Note:  the original list `my_list` will be modified and will contain the added third element with the sum of the previous two numbers.