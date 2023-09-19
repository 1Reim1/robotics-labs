def main():
    print("Enter 5 numbers")
    summa = 0
    for _ in range(5):
        number = int(input())
        if number % 2 == 1:
            summa += number
    print(f"Sum: {summa}")


if __name__ == "__main__":
    main()
