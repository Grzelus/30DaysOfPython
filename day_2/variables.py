import math

#Day 2: 30 Days of python programming

first_name = 'Kacper'
last_name = 'Grzelak'
fullname = first_name + ' ' + last_name
country = 'Poland'
city = 'Poznan'
age = 21
year = 2025
is_married = True
is_true = True
is_light_on = True
friend_name, girlfriend_name = 'Kuba', 'Samanta'

for var in [first_name, last_name, fullname, country, city, age, year, is_married, is_true, is_light_on, friend_name, girlfriend_name]:
    print(type(var))

first_name_len = len(first_name)
print(first_name_len)

is_first_name_len_longer = first_name_len > len(last_name)
print(f"Is my firstname longer than lastname: {is_first_name_len_longer}")

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
reminder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

for var in [total, diff, product, division, reminder, exp, floor_division]:
    print(var)

circle_radius = float(input("Circle's raduis: "))

def calculate_circle_area(radius: float):
    return math.pi * radius ** 2

def calculate_circle_circumference(radius: float):
    return 2 * math.pi * radius

area_of_circle = calculate_circle_area(circle_radius)
circum_of_circle = calculate_circle_circumference(circle_radius)

print(area_of_circle, circum_of_circle)

user_first_name, user_last_name, user_country, user_age = (input("Insert your firstname, lastname, country, age... (separate using space): ")).split(" ")
print(user_first_name, user_last_name, user_country, user_age)