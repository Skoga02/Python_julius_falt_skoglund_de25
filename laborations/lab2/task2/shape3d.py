class Shape3d:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        for name, value in {"x": x, "y": y, "z": z}.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be numeric")
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x
        
    @property
    def y(self):
        return self._y
        
    @property
    def z(self):
        return self._z

    # Gives us the possiblity to move around in 3D
    def translate(self, dx: float, dy: float, dz: float):
        if not all(isinstance(v, (int, float)) for v in [dx, dy, dz]):
            raise TypeError("dx, dy and dz must be numeric values")
        self._x += dx
        self._y += dy
        self._z += dz

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self._x}, y={self._y}, z={self._z})"
    
    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self._x}, {self._y}, {self._z})"
    
    # this is to compare based on item volume
    def __eq__(self, other):
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume == other.volume
    
    def __lt__(self, other):
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume < other.volume

    def __le__(self, other):
        return self == other or self < other 
    
    def __gt__(self, other):
        return not self <= other 
    
    def __ge__(self, other):
        return not self < other 
    
    @property
    def volume(self):
        raise NotImplemented
    
    @property
    def surface_area(self):
        raise NotImplemented