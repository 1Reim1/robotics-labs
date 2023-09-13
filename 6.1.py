import os

DIRECTORY = "6"


def main():
    mode = input("""1 - тільки файли
2 - тільки папки
3 - все
""")
    filenames = os.listdir(DIRECTORY)
    if mode == "1":
        filenames = [f for f in filenames if os.path.isfile(os.path.join(DIRECTORY, f))]
    elif mode == "2":
        filenames = [f for f in filenames if os.path.isdir(os.path.join(DIRECTORY, f))]
    print(filenames)


if __name__ == "__main__":
    main()
