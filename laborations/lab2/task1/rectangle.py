from shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0):
        super().__init__(x, y)
        
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric values")
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        
        self._width = width 
        self._height = height

    @property 
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height

    @property
    def area(self) -> float:
        return self._width * self._height
    
    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)
    
    def is_square(self) -> bool:
        return self._width == self._height
    
    def __repr__(self):
        return f"Rectangle (width={self._width}, height={self._height}, x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"Rectangle ({self._width}x{self._height}) at ({self.x}, {self.y})"
    
    # Qucik visual easier to debug and get a overview
    def draw(self): 
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle as RectPatch

        fig, ax = plt.subplots()

        rect = RectPatch(
            (self.x - self._width / 2, self.y - self._height / 2),
            self._width, self._height, fill=False, edgecolor='blue', linewidth=2)
        
        ax.add_patch(rect)

        padding = max(self._width, self._height) * 0.5
        ax.set_xlim(self.x - self._width / 2 - padding, self.x + self._width / 2 + padding)
        ax.set_ylim(self.y - self._height / 2 - padding, self.y + self._height / 2 + padding)


        ax.set_aspect('equal', adjustable='box')
        plt.title(str(self))
        plt.grid(True)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        plt.show()


    