def main():
    a = int(input("a: "))
    b = int(input("b: "))
    print(f"Кратні: {'Так' if a % b == 0 or b % a == 0 else 'Ні'}")


if __name__ == "__main__":
    main()
