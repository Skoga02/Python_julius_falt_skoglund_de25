from cube import Cube
from sphere import Sphere

cube1 = Cube(side=1)
cube2 = Cube(side=2)
sphere1 = Sphere(radius=1)
sphere2 = Sphere(radius=2)

print("Cube 1 volume:", cube1.volume)
print("sphere1 volume:", sphere1.volume)
print("Cube == sphere:", cube1 == sphere1)
print("sphere2 >  sphere2:", sphere2 > sphere1)

cube1.translate(2, 3, 4)
print("Cube new position:", (cube1.x, cube1.y, cube1.z))

try:
    Cube(side="three")
except TypeError as e:
    print("Caught error:", e)

try:
    Sphere(radius=-1)
except ValueError as e:
    print("Caught error:", e)