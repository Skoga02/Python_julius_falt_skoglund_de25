from pytest import raises
from circle import Circle 
from rectangle import Rectangle 

circle1 = Circle (x=0, y=0, radius=1)
circle2= Circle(x=1, y=1, radius=1)
rectangle = Rectangle(x=0, y=0, width=1, height=1)

print(circle1 == circle2)

print(circle2 == rectangle)

circle1.translate(5, 3)
print(circle1.x, circle1.y)

circle3 = Circle(radius=3)
print(circle3 >= circle1)

try:
    circle4 = Circle(radius="5")
except TypeError:
    print("Radius must be a numerci value")