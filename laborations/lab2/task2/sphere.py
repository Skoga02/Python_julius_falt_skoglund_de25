import math
from shape3d import Shape3d

class Sphere(Shape3d):
    def __init__(self, radius: float, x: float = 0, y: float = 0, z: float = 0):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be numeriv")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius


    @property
    def radius(self):
        return self._radius
    
    @property 
    def volume(self) -> float:
        return (4 / 3) * math.pi * (self._radius ** 3)
    
    @property
    def surface_area(self) -> bool:
        return self._radius == 1
    
    def __repr__(self):
        return f"Sphere(radius={self._radius}, x={self.x}, y={self.y}. z={self.z})"
    
    def __str__(self):
        return f"Sphere (rafius={self._radius}, at {self.x}, {self.y}, {self.z})"

