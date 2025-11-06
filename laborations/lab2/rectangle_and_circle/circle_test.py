import pytest
import math
from circle import Circle

def test_circle_creation():
    c = Circle(radius=2, x= 1, y=1)
    assert c.radius == 2
    assert c.x == 1
    assert c.y == 1

def test_circle_invalid_radius_type():
    with pytest.raises(TypeError):
        Circle(radius='big')

def test_circle_invalid_radius_value():
    with pytest.raises(ValueError):
        Circle(radius=0)

def test_circle_area_and_perimeter():
    c = Circle(radius=1)
    assert round(c.area, 5) == round(math.pi, 5)
    assert round(c.perimeter, 5) == round(2 * math.pi, 5)

def test_is_circle():
    c = Circle(radius=1)
    assert c.is_unit_circle()

def test_circle_comparisn():
    c1 = Circle(radius=1)
    c2 = Circle(radius=2)
    assert c1 < c2
    assert c2 > c1
    assert not c1 == c2