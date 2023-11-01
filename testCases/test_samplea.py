# test_math_operations.py
import pytest


@pytest.mark.smoke
@pytest.mark.regression
# Addition
def add(x, y):
    return x + y


@pytest.mark.smoke
@pytest.mark.regression
# Subtraction
def subtract(x, y):
    return x - y


@pytest.mark.smoke
@pytest.mark.regression
# Multiplication
def multiply(x, y):
    return x * y


@pytest.mark.smoke
@pytest.mark.regression
# Division
def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y


@pytest.mark.regression
# Calculate the area of a circle
def circle_area(radius):
    import math
    return math.pi * (radius ** 2)


@pytest.mark.regression
# Calculate the area of a square
def square_area(side_length):
    return side_length ** 2


@pytest.mark.regression
# Parameterized tests for addition
@pytest.mark.parametrize("x, y, expected", [(2, 3, 5), (0, 0, 0), (-1, 1, 0)])
def test_add(x, y, expected):
    assert add(x, y) == expected


@pytest.mark.regression
# Parameterized tests for subtraction
@pytest.mark.parametrize("x, y, expected", [(5, 3, 2), (0, 0, 0), (1, 3, -2)])
def test_subtract(x, y, expected):
    assert subtract(x, y) == expected


@pytest.mark.regression
# Parameterized tests for multiplication
@pytest.mark.parametrize("x, y, expected", [(2, 3, 6), (0, 5, 0), (-4, 2, -8)])
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected


@pytest.mark.regression
# Parameterized tests for division
@pytest.mark.parametrize("x, y, expected", [(6, 3, 2), (0, 5, 0)])
def test_divide(x, y, expected):
    assert divide(x, y) == expected


@pytest.mark.skip(reason="Skipping this test for a specific reason")
# @pytest.mark.regression
# Parameterized tests for circle area calculation
@pytest.mark.parametrize("radius, expected", [(2, 12.566370614359172), (0, 0), (5, 78.53981633974483)])
def test_circle_area(radius, expected):
    assert circle_area(radius) == expected


@pytest.mark.skip(reason="Skipping this test for a specific reason")
# @pytest.mark.regression
# Parameterized tests for square area calculation
@pytest.mark.parametrize("side_length, expected", [(2, 4), (0, 0), (5, 25)])
def test_square_area(side_length, expected):
    assert square_area(side_length) == expected
