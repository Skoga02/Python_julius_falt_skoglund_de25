from abc import ABC, abstractmethod

class Shape(ABC):
    """
    A parent class for 2D shapes that provides common properties and methods.
    """
    def __init__(self, x: float = 0, y: float = 0) -> None:
        # Initialize position coordinates.
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        # Read-only property for the x-coordinate.
        return self._x

    @property
    def y(self) -> float:
        # Read-only property for the y-coordinate.
        return self._y

    @property
    @abstractmethod
    def area(self) -> float: 
        """
        Abstract property for shape's area.
        Must be implemented by subclasses.
        """
        pass 

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """
        Abstract property for shape's perimeter.
        Must be implementd by subclass.
        """
        pass

    def __eq__(self, other) -> bool:
        # Checks if two shapes have the same area.
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area == other.area
    
    def __lt__(self, other) -> bool:
        # Checks if this shapes area is less than anothers
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area < other.area
    
    def __le__(self, other) -> bool:
        # less-than or equal comparison of area. 
        return self == other or self < other
    
    def __gt__(self, other) -> bool:
        # Greater-than area. 
        return not self <= other
    
    def __ge__(self, other) -> bool: 
        # Greater-than or equal area. 
        return not self < other
    
    def translate(self, dx: float, dy: float) -> None:
        """
        Moves the shape in 2D space by the specified cordinates.
        Validates that dx an dy are numeric.
        """
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numeric values.")
        self._x += dx
        self._y += dy 

    def __repr__(self) -> str:
        #Official string representation of the shape.
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"
    
    def __str__(self) -> str:
        # Readable string describing the shapes position
        return f"{self.__class__.__name__} centered at ({self._x}, {self._y})"
    
