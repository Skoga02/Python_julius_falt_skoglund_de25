import pytest
from cube import Cube

def test_cube_creation():
    c = Cube(side=3)
    assert c.side == 3

def test_invalid_side_type():
    with pytest.raises(TypeError):
        Cube (side="3")

def test_invalid_side_value():
    with pytest.raises(ValueError):
        Cube (side=0)

def test_cube_volume_and_surface_area():
    c = Cube(side=2)
    assert c.volume == 8
    assert c.surface_area == 24

def test_comparisons():
    c1 = Cube(side=2)
    c2 = Cube(side=3)
    assert c1 < c2
    assert c2 > c1