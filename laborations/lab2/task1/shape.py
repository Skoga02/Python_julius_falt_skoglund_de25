from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    # make getter private (public: read_only)
    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    # abstract properties 
    @property
    @abstractmethod
    def area(self) -> float: 
        pass 

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    # operator overloads test
    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area == other.area
    
    def __lt__(self, other): 
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area < other.area
    
    def __le__(self, other):
        return self == other or self < other
    
    def __gt__(self, other):
        return not self <= other
    
    def __ge__(self, other): 
        return not self < other
    
    # tranlsating part of the code is to enable a change of cordinates (x, y) for a class
    
    def translate(self, dx: float, dy: float):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numeric values.")
        self._x += dx
        self._y += dy 

    # representations part 

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"
    
    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self._x}, {self._y})"
    
