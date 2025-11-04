from shape3d import Shape3d

class Cube(Shape3d):
    def __init__(self, side:  float, x: float = 0, y: float = 0, z: float = 0):
        super().__init__(x, y, z)
        if not isinstance(side, (int, float)):
            raise TypeError("Side length must be numeric")
        if side <= 0:
            raise ValueError("Side length must bee positive")
        self._side = side

    @property
    def side(self):
        return self._side 
    
    @property
    def volume(self) -> float:
        return self._side ** 3

    @property
    def surface_area(self) -> float:
        return 6 * (self._side ** 2)
    
    def is_unit_cube(self) -> bool:
        return self._side == 1
    
    def __repr__(self):
        return f"Cube(side={self._side}, x={self.x}, y={self.y}, z={self.z})"
    
    def __str__(self):
        return f"Cube (side={self._side}) at ({self.x}, {self.y}, {self.z})"
    
    