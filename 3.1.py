import re


def main():
    s = input()
    print(f"Кількість символів: {len(s)}")
    words = len(re.findall('\\w+', s))
    print(f"Кількість слів: {words}")


if __name__ == "__main__":
    main()
