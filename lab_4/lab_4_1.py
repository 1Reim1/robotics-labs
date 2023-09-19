import random


def main():
    number = random.randint(1, 9)
    while int(input("Guess the number: ")) != number:
        pass
    print("You won")


if __name__ == "__main__":
    main()
