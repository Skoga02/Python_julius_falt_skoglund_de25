import pytest 
import math
from sphere import Sphere

def test_sphere_creation():
    s = Sphere(radius=2, x=1, y=1, z=1)
    assert s.radius == 2
    assert s.x == 1
    assert s.y == 1
    assert s.z == 1

def test_invalid_radius_type():
    with pytest.raises(TypeError):
        Sphere(radius="2")

def test_invalid_radius_value():
    with pytest.raises(ValueError):
        Sphere(radius=0)

def test_spher_volume_and_surface_area():
    s = Sphere(radius=1)
    assert math.isclose(s.volume, (4/3) * math.pi * 1**3)
    assert s.surface_area == pytest.approx(4 * math.pi)

def test_comparison():
    s1 = Sphere(radius=1)
    s2 = Sphere(radius=2)
    assert s1 < s2
    assert s2 > s1
    assert not s1 == s2