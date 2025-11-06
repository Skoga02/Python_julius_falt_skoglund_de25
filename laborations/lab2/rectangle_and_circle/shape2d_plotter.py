import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectPatch , Circle as CirclePatch 
from rectangle import Rectangle 
from circle import Circle

class Shape2d_plotter:
    """
    Class for managing and plotting 2D shapes using matplotlib
    """

    def __init__(self) -> None:
        self._shapes = []

    def add_shape(self, shape) -> None:
        if not isinstance(shape, (Circle, Rectangle)):
            raise TypeError("Shape must be an instanve of a Circle or Rectangle")
        self._shapes.append(shape)

    def clear(self) -> None:
        self._shapes.clear()

    def plot(self, show_center=True) -> None:
        """
        Plots all shapes using matplotlib.
        If show_center is True, plots the center points of the shape.
        """
        fig, ax = plt.subplots()

        for shape in self._shapes:
            if isinstance(shape, Circle):
                patch = CirclePatch(
                    (shape.x, shape.y),
                    shape.radius,
                    fill=False,
                    edgecolor='red',
                    linewidth=2
                )
                ax.add_patch(patch)
                if show_center:
                    ax.plot(shape.x, shape.y, 'ro')

            elif isinstance(shape, Rectangle):
                patch = RectPatch(
                    (shape.x - shape.width / 2, shape.y - shape.height / 2),
                    shape.width,
                    shape.height,
                    fill=False,
                    edgecolor='blue',
                    linewidth=2
                )
                ax.add_patch(patch)
                if show_center:
                    ax.plot(shape.x, shape.y, 'ro')

        all_x = [shape.x for shape in self._shapes]
        all_y = [shape.y for shape in self._shapes]
        if all_x and all_y:
            x_min = min(all_x) - 5
            x_max = max(all_x) + 5
            y_min = min(all_y) - 5
            y_max = max(all_y) + 5
            ax.set_xlim(x_min, x_max)
            ax.set_ylim(y_min, y_max)
        
        ax.set_aspect('equal', adjustable='box')
        plt.title("2D Shapes Plotter")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.show()


# Qucik and easy way to display plotters functinality.

if __name__ == "__main__":
    from circle import Circle
    from rectangle import Rectangle

    plotter = Shape2d_plotter()
    plotter.add_shape(Circle(x=0, y=0, radius=2))
    plotter.add_shape(Rectangle(x=3, y=2, width=4, height=1))
    plotter.add_shape(Rectangle(x= 2, y=1, width=4, height=1))
    plotter.plot()