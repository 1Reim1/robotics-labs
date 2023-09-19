def main():
    a = float(input("a: "))
    b = float(input("b: "))
    if a == b:
        print("This is a square")
    print(f"Perimeter: {(a + b) * 2}")
    print(f"Area: {a * b}")


if __name__ == "__main__":
    main()
