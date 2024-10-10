"""
General geometry-related functions

Syntax:

area = circle_area(diameter)
area = rectangle_area(length, width)
area = square_area(side)
"""
import math   # load math.py

PI = math.pi

Number = int | float

def circle_area(diameter: Number) -> float:
    """
    Compute the area of a circle from a given diameter

    :param diameter: Diameter of circle
    :return: Area of circle
    """
    radius = diameter / 2
    return PI * (radius ** 2)

def rectangle_area(length: Number, width: Number) -> Number:
    """
    Compute the area of a rectangle.

    :param length:  length of longer side
    :param width:   length of shorter side
    :return: Area of rectangle
    """
    return length * width

def square_area(side: Number) -> Number:
    """
    Compute area of a square.

    :param side: Length of one side
    :return: Area of square
    """
    return side ** 2

print(f"my name is {__name__}")

if __name__ == "__main__":
    area1 = square_area(15)
    print(f"area1: {area1}")
    
    area2 = circle_area(22)
    print(f"area2: {area2}")
    
    area3 = rectangle_area(9, 13)
    print(f"area3: {area3}")
