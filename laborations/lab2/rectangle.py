from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        super().__init__(x, y)
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width 
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        return self.width == self.height
    
    def __repr__(self):
        return f"Rectangle (width={self.width}, height={self.height}, x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"Rectangle ({self.width}x{self.height}) at ({self.x}, {self.y})"
    
    def draw(self): 
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle as RectPatch

        fig, ax = plt.subplots()
        ax.add_patch(RectPatch(
            (self.x - self.width / 2, self.y - self.height / 2),
            self.width, self.height, fill=False, edgecolor='blue', linewidth=2))
        ax.set_aspect('equal')
        plt.title(str(self))
        plt.show