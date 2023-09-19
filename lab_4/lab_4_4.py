def main():
    number1 = 0
    number2 = 1
    next_number = number2
    while next_number <= 50:
        print(next_number)
        number1, number2 = number2, next_number
        next_number = number1 + number2


if __name__ == "__main__":
    main()
