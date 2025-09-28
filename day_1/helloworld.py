import sys
import math

#exercise 1
print("Python version:")
print(sys.version)

#exercise 2
print(4+3)
print(4-3)
print(4*3)
print(4%3)
print(4/3)
print(4**3)
print(4//3)

#exercise 3
print("Kacper")
print('Grzelak')
print('''Poland''')
print("""I am enjoying 30 days of python""")

#exercise 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabbeneh', 'Python', 'Finland']))
print(type("Kacper"))
print(type('Grzelak'))
print(type('Poland'))

#other examples
number = 5
float = 4.7
complex = 4-4j
string = "house"
boolean = False
list = [5,3,4]
set = {4,3,5}
_tuple = (4,5,6) #need tuple object later
dictionary = {"phone": "123-132-421"}

for var in [number, float, complex,string,boolean,list, _tuple, set, dictionary]:
    print(f'''var: {var}
var type: {type(var)}''')
    
def euclidian(point1: tuple, point2: tuple):
    x1,y1,x2,y2 =  [value for value in point1 + point2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(euclidian((2,3), (10,8)))
