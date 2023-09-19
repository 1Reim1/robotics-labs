import re


def main():
    s = input()
    print(f"Number of characters: {len(s)}")
    words = len(re.findall('\\w+', s))
    print(f"Number of words: {words}")


if __name__ == "__main__":
    main()
