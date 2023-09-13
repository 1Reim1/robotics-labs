def main():
    a = float(input("a: "))
    b = float(input("b: "))
    if a == b:
        print("Це квадрат")
    print(f"Периметр: {(a + b) * 2}")
    print(f"Площа: {a * b}")


if __name__ == "__main__":
    main()
