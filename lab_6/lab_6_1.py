import os

DIRECTORY = "folder"


def main():
    mode = input("""1 - only files
2 - only folders
3 - all
""")
    filenames = os.listdir(DIRECTORY)
    if mode == "1":
        filenames = [f for f in filenames if os.path.isfile(os.path.join(DIRECTORY, f))]
    elif mode == "2":
        filenames = [f for f in filenames if os.path.isdir(os.path.join(DIRECTORY, f))]
    print(filenames)


if __name__ == "__main__":
    main()
