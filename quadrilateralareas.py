def square(side: float) -> float:

    return side ** 2

def rectangle(width: float, height: float) -> float:

    return width * height

def parallelogram(side: float, height: float) -> float:

    return side * height

def trapezium(height: float, width_1: float, width_2: float) -> float:

    return 0.5 * height * ( width_1 + width_2 )

def rhombus(height: float, width: float) -> float:

    return 0.5 * height * width

def kite(height: float, width: float) -> float:

    return 0.5 * height * width