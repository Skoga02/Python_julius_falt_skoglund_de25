from shape import Shape
import math

class Circle(Shape):
    """
    Class representing a circle with a radius and positon. 
    Inherits from Shape.
    """
    def __init__(self, radius: float, x: float = 0, y: float = 0) -> None:
        # Initializes a circle with a given radius and position. Check if radius is numeric and positiv
        super().__init__(x, y)
        
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value")

        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = radius

    @property
    def radius(self) -> float:
        # Read-only property for the radius.
        return self._radius

    @property
    def area(self) -> float:
        # Claculates and returns the area.
        return math.pi * self._radius ** 2

    @property
    def perimeter(self) -> float:
        # Claculates and returns the perimeter.
        return 2 * math.pi * self._radius
    
    def is_unit_circle(self) -> bool:
        # Checks if the circle is a unit circle, centerd at the origin.
        return self._radius == 1 and self.x == 0 and self.y == 0
    
    def __repr__(self) -> str:
        # Official string representation of the circle
        return f"Circle(radius={self._radius}, x={self.x}, y={self.y})"
    
    def __str__(self) -> str:
        # readable string 
        return f"Circle (r={self._radius}) at ({self.x}, {self.y})"