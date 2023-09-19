from math import sqrt


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = b * b - 4 * a * c
    if d < 0:
        print("There are no solutions")
        return
    print(f"x1: {(-b + sqrt(d)) / (2 * a)}")
    print(f"x2: {(-b - sqrt(d)) / (2 * a)}")


if __name__ == "__main__":
    main()
