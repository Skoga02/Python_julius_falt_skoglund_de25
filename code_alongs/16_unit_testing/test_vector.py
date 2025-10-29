# py-test
from pytest import raises
from vector import Vector

def test_valid_init():
    v = Vector(1,2)
    assert v.numbers == (1,2)


# test negative values in init
def test_negative_value():
    v = Vector(-1, -2, 4)
    assert v.numbers == (-1, -2, 4)


# test string in the init 
def test_string_in_init():
    with raises(TypeError):
        Vector(1, "a", 5)


# test len() funciton 
def test_len_function():
    v = Vector(3, 4, 5)
    assert len(v) == 3

# test diffrent len() function
def test_len_dif_function():
    vectors = (Vector(1,2), Vector(1), Vector(1, 2, 3), Vector(1, 2, 3, 4))
    excepted_lengths = (2, 1, 3, 4)

    for vector, excepted_length in zip(vectors, excepted_lengths):
        assert len(vector) == excepted_length

# test abs() function
def test_abs_function():
    v = Vector(3, 4,)
    assert abs(v) == 5


def test_empty_vector_fail():
    with raises(ValueError):
        Vector()

