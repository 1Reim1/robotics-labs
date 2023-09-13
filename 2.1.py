def main():
    print("Введіть 5 чисел")
    summa = 0
    for _ in range(5):
        number = int(input())
        if number % 2 == 1:
            summa += number
    print(f"Сума: {summa}")


if __name__ == "__main__":
    main()
