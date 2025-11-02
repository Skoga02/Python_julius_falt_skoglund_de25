from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius: float, x: float = 0, y: float = 0):
        super().__init__(x, y)
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * self.radius

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def is_unit_circle(self) -> bool:
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    def __repr__(self):
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"Circle (r={self.radius}) at ({self.x}, {self.y})"
    
    def draw(self): 
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle as CirclePatch

        fig, ax = plt.subplots()
        ax.add_patch(CirclePatch((self.x, self.y), self.radius, fill=False, edgecolor='red', linewidth=2))
        ax.set_aspect('equal')
        plt.title(str(self))
        plt.show()