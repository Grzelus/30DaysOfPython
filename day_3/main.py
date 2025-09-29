def main():
    import math
    import matplotlib.pyplot as plt
    import numpy as np

    age = 21
    height = 1.73
    complex_number = 4 -3j

    def calculate_triangle_area(base: float, height: float):
        return base * height / 2

    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    print(f"Area of this triangle: {calculate_triangle_area(base, height)}")

    sides = []

    for i in range(0,3):
        side = float(input(f"Enter {i+1} side: "))
        sides.append(side)

    print(f"Perimeter of the triangle is {sum(sides)}")

    a, b = map(float, input("Enter width and height of rectangle (separated by space): ").split(" "))

    print(f"Area: {a * b}, Perimeter: {2 * (a + b)}")

    radius = float(input("Radius: "))

    print(f"Area: {math.pi * radius ** 2}, Circumference: {2 * math.pi * radius}")

    m=2
    b=-2

    x_intercept = -b/2
    y_intercept = b

    print(f"x intercept: ({x_intercept}, 0), y intercept: (0, {float(y_intercept)})")

    point1,point2 = (2,2), (6,10)

    def calculate_slope(point1: tuple, point2: tuple):
        x1, y1 = point1
        x2, y2 = point2

        m = (y2 - y1)/(x2 - x1)
        b = y1 - m * x1

        return m, b

    def find_euclidean_distance(point1: tuple, point2: tuple):
        x1, y1 = point1
        x2, y2 = point2

        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    calculated_m, calculated_b = calculate_slope(point1, point2)

    print(f"Slope: {calculate_slope(point1, point2)}, Euclidean distance: {find_euclidean_distance(point1, point2)}")
    print(f"slope1: y = {float(m)}x + {float(b)}")
    print(f"slope2: y = {calculated_m}x + {calculated_b}")


    x = np.linspace(-10,10,101)
    y1 = m * x + b
    y2 = calculated_m * x + calculated_b
    y3 = x**2 + 6*x + 9

    for index, y in enumerate(y3):
        if y == 0:
            print(f"for x = {x[index]} slope = 0")

    plt.plot(x,y1, label='1st')
    plt.plot(x,y2, label="2nd")
    plt.plot(x, y3, label='3th')

    plt.axhline()
    plt.axvline()

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of slopes')
    plt.legend()
    plt.grid(True)

    plt.show()

    print('python' == 'dragon')

    is_on_in = 'on' in 'python' and 'on' in 'dragon'
    if is_on_in:
        print('dragon and python contain \'on\'')

    sentance = 'I hope this course is not full of jargon.'
    if 'jargon' in sentance:
        print('sentance contains jargon')

    print('on' not in 'dragon' and 'on' not in 'python')

    length = len('python')
    print(length, float(length), str(length))

    def is_even(number: int):
        return number % 2 == 0

    print(is_even(43))

    print(7//3 == int(2.7))
    print(type('10') == type(10))
    print(int(float('9.8')) == 10)

    def calculate_weekly_pay(hours: int,rate_per_hour:int):
        if hours > 168:
            print('Invalid amount of hours.')
            return None
        return hours*rate_per_hour

    def calculate_seconds_of_life(years:int):
        if years > 100:
            print('Invalid amount of years.')
            return None
        return years*365.25*24*3600

    for i in range(1, 6):
        print(f"{i} ", end='')
        for j in range(0,4):
            print(f"{i** j} ", end='')
        print('')

if __name__ == '__main__':
    main()
