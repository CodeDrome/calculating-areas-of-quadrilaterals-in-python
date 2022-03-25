import quadrilateralareas


def main():

    print("---------------------------")
    print("| codedrome.com           |")
    print("| Areas of Quadrilaterals |")
    print("---------------------------\n")

    square = { "side": 12, "area": 0 }
    square["area"] = quadrilateralareas.square(square["side"])
    print(f"square: {square}")

    print()

    rectangle = { "width": 16, "height": 8, "area": 0 }
    rectangle["area"] = quadrilateralareas.rectangle(rectangle["width"], rectangle["height"])
    print(f"rectangle: {rectangle}")

    print()

    parallelogram = { "side": 12, "height": 12, "area": 0 }
    parallelogram["area"] = quadrilateralareas.parallelogram(parallelogram["side"], parallelogram["height"])
    print(f"parallelogram: {parallelogram}")

    print()

    trapezium = { "width_1": 12, "width_2": 16, "height": 12, "area": 0 }
    trapezium["area"] = quadrilateralareas.trapezium(trapezium["width_1"], trapezium["width_2"], trapezium["height"],)
    print(f"trapezium: {trapezium}")

    print()

    rhombus = { "height": 24, "width": 10, "area": 0 }
    rhombus["area"] = quadrilateralareas.rhombus(rhombus["height"], rhombus["width"])
    print(f"rhombus: {rhombus}")

    print()

    kite = { "height": 40, "width": 24, "area": 0 }
    kite["area"] = quadrilateralareas.kite(kite["height"], kite["width"])
    print(f"kite: {kite}")

main()
