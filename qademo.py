import quadrilateralareas as qa


def main():

    print("---------------------------")
    print("| codedrome.com           |")
    print("| Areas of Quadrilaterals |")
    print("---------------------------\n")

    square = { "side": 12, "area": 0 }
    square["area"] = qa.square(square["side"])
    print(f"square: {square}")

    print()

    rectangle = { "width": 16, "height": 8, "area": 0 }
    rectangle["area"] = qa.rectangle(rectangle["width"], rectangle["height"])
    print(f"rectangle: {rectangle}")

    print()

    parallelogram = { "side": 12, "height": 12, "area": 0 }
    parallelogram["area"] = qa.parallelogram(parallelogram["side"], parallelogram["height"])
    print(f"parallelogram: {parallelogram}")

    print()

    trapezium = { "width_1": 12, "width_2": 16, "height": 12, "area": 0 }
    trapezium["area"] = qa.trapezium(trapezium["width_1"], trapezium["width_2"], trapezium["height"],)
    print(f"trapezium: {trapezium}")

    print()

    rhombus = { "height": 24, "width": 10, "area": 0 }
    rhombus["area"] = qa.rhombus(rhombus["height"], rhombus["width"])
    print(f"rhombus: {rhombus}")

    print()

    kite = { "height": 40, "width": 24, "area": 0 }
    kite["area"] = qa.kite(kite["height"], kite["width"])
    print(f"kite: {kite}")


if __name__ == "__main__":

    main()