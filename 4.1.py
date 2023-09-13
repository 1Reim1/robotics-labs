import random


def main():
    number = random.randint(1, 9)
    while int(input("Вгадай число: ")) != number:
        pass
    print("Ви виграли")


if __name__ == "__main__":
    main()
