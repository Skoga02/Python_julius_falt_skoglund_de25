from shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius: float, x: float = 0, y: float = 0):
        super().__init__(x, y)
        
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value")

        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def area(self) -> float:
        return math.pi * self._radius ** 2

    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius
    
    def is_unit_circle(self) -> bool:
        return self._radius == 1 and self.x == 0 and self.y == 0
    
    def __repr__(self):
        return f"Circle(radius={self._radius}, x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"Circle (r={self._radius}) at ({self.x}, {self.y})"
    
    def draw(self): 
        import matplotlib.pyplot as plt
        from matplotlib.patches import Circle as CirclePatch

        fig, ax = plt.subplots()

        circle = CirclePatch(
            (self.x, self.y),
            self._radius,
            fill=False,
            edgecolor='red',
            linewidth=2
        )
        ax.add_patch(circle)
        
        padding = self._radius * 0.5 
        ax.set_xlim(self.x - self._radius - padding, self.x + self._radius + padding)
        ax.set_ylim(self.y - self._radius - padding, self.y + self._radius + padding)

        ax.set_aspect('equal', adjustable='box')
        plt.title(str(self))
        plt.grid(True)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")

        plt.show()