import math
from shape3d import Shape3d

class Sphere(Shape3d):
    """
    A sphere shape with a specified radius and position in 3D.
    Inherits from Shape3D.
    """
    def __init__(self, radius: float, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y, z)
        if not isinstance(radius, (int, float)):
            # Validate that radius is numeric
            raise TypeError("Radius must be numeriv")
        if radius <= 0:
            # Validate that radius is positive
            raise ValueError("Radius must be positive")
        # Stores radius as a private attribute
        self._radius = radius

    @property
    def radius(self) -> float:
        # Get the radius of the sphere.
        return self._radius
    
    @property 
    def volume(self) -> float:
        # Calculate and return the volume of the sphere.
        return (4 / 3) * math.pi * (self._radius ** 3)
    
    @property
    def surface_area(self) -> float:
        # Calculate and return the surface area of the sphere.
        return 4 * math.pi * self._radius**2
    
    def __repr__(self) -> str:
        # Official string description of the sphere.
        return f"Sphere(radius={self._radius}, x={self.x}, y={self.y}, z={self.z})"
    
    def __str__(self) -> str:
        # Readable string description of the sphere.
        return f"Sphere (rafius={self._radius}, at {self.x}, {self.y}, {self.z})"

