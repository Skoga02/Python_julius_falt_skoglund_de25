from shape import Shape

class Rectangle(Shape):
    """
    A Rectangle shape with a fixed width and height. Inherits from parent class Shape.
    """
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0) -> None:
        super().__init__(x, y)
        
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            # Validates that width and height are numeric.
            raise TypeError("Width and height must be numeric values")
        
        if width <= 0 or height <= 0:
            # Validates that width and height are positive.
            raise ValueError("width and height must be positive")
        # Stores width and height as private attributes
        self._width = width 
        self._height = height

    @property 
    def width(self) -> float:
        # Get width of the rectangle.
        return self._width
    
    @property
    def height(self) -> float:
        # Get height of the rectangle.
        return self._height

    @property
    def area(self) -> float:
        # Calculate and return the area.
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        # Calculate and return the perimeter.
        return 2 * (self._width + self._height)
    
    def is_square(self) -> bool:
        # Check if the rectangle is square.
        return self._width == self._height
    
    def __repr__(self) -> str:
        # Official string representation of the rectangle.
        return f"Rectangle (width={self._width}, height={self._height}, x={self.x}, y={self.y})"
    
    def __str__(self) -> str:
        # Readable string description of the rectangle.
        return f"Rectangle ({self._width}x{self._height}) at ({self.x}, {self.y})"