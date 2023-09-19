def main():
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"These numbers are multiples: {'Yes' if a % b == 0 or b % a == 0 else 'No'}")


if __name__ == "__main__":
    main()
