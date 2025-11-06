import pytest
from rectangle import Rectangle 

def test_rectangle_creation():
    r = Rectangle(width=3, height=4)
    assert r.width == 3
    assert r.height == 4

def test_rectangle_invalid_type():
    with pytest.raises(TypeError):
        Rectangle(width="4", height=3)

def test_rectangle_invalid_value():
    with pytest.raises(ValueError):
        Rectangle(width=-2, height=3)

def test_area_and_perimeter():
    r = Rectangle(width=3, height=4)
    assert r.area == 12
    assert r.perimeter == 14

def test_is_square():
    r = Rectangle(width=5, height=5)
    assert r.is_square()

def test_rectangle_comparison():
    r1 = Rectangle(width=2, height=2)
    r2 = Rectangle(width=3, height=3)
    assert r1 < r2
    assert r2 > r1
    assert not r1 == r2