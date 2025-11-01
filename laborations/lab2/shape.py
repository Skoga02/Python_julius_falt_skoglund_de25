from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y
    
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
    
    # translating part of the code 
    
    def translate(self, dx: float, dy: float):
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numeric values.")
        self.x += dx
        self.dy += dy 

    # representations part 

    def __repr__(self):
        return f"{self,__class__.__name__}(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"{self.__class__.__name__} centerd at ({self.x}, {self.y})"
    
