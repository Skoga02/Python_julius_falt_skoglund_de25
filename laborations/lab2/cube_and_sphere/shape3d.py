class Shape3d:
    """
    A parent class for 3D shapes that provides common properties and methods.
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        # Initialise position coordinates with validation
        for name, value in {"x": x, "y": y, "z": z}.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"{name} must be numeric")
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x
        
    @property
    def y(self) -> float:
        return self._y
        
    @property
    def z(self) -> float:
        return self._z


    def translate(self, dx: float = 0, dy: float = 0, dz: float = 0) -> None:
        """
        Translate to move the shape in 3D space by specific cordinates.
        """
        if not all(isinstance(v, (int, float)) for v in [dx, dy, dz]):
            raise TypeError("dx, dy and dz must be numeric values")
        self._x += dx
        self._y += dy
        self._z += dz

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self._x}, y={self._y}, z={self._z})"
    
    def __str__(self) -> str:
        # readble string.
        return f"{self.__class__.__name__} centered at ({self._x}, {self._y}, {self._z})"
    
    def __eq__(self, other) -> bool:
        # compares shape based on volume.
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume == other.volume
    
    def __lt__(self, other) -> bool:
        # Less-than comparison based on volume.
        if not isinstance(other, Shape3d):
            return NotImplemented
        return self.volume < other.volume

    def __le__(self, other) -> bool:
        # Greater-than comparison.
        return self == other or self < other 
    
    def __gt__(self, other) -> bool:
        # Greater-than comparison.
        return not self <= other 
    
    def __ge__(self, other) -> bool:
        # Greater-than or equal comparison.
        return not self < other 
    
    @property
    def volume(self) -> float:
        # Placeholder for volume property, to be implemented by subclass.
        raise NotImplemented
    
    @property
    def surface_area(self) -> float:
        # Placeholder for surface area property, to be implemented by subclass.
        raise NotImplemented