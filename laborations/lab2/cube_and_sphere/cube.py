from shape3d import Shape3d

class Cube(Shape3d):
    """
    A cube with a specified side length and position in 3D.
    Inherits from shape3D.
    """
    def __init__(self, side:  float, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y, z)
        if not isinstance(side, (int, float)):
            # Validates that side is numeric.
            raise TypeError("Side length must be numeric")
        if side <= 0:
            # Validates that side length is positive.
            raise ValueError("Side length must bee positive")
        # Stores side as a private attribute.
        self._side = side

    @property
    def side(self) -> float:
        # Get the side length of the cube.
        return self._side 
    
    @property
    def volume(self) -> float:
        #Calculate and return the volume of the cube.
        return self._side ** 3

    @property
    def surface_area(self) -> float:
        # Calculate and return the surface area of the cube.
        return 6 * (self._side ** 2)
    
    def is_unit_cube(self) -> bool:
        # Check if the cube is a unit cube.
        return self._side == 1
    
    def __repr__(self) -> str:
        # Official strinf representation of the cube.
        return f"Cube(side={self._side}, x={self.x}, y={self.y}, z={self.z})"
    
    def __str__(self) -> str:
        # Readable string description of the cube.
        return f"Cube (side={self._side}) at ({self.x}, {self.y}, {self.z})"
    
    