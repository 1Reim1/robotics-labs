import os.path


def main():
    filename = r"6\file.txt"
    filename_1 = r"6\first.txt"
    filename_2 = r"6\second.txt"
    text = 'This is very cool\ntwo lines text'
    with open(filename, "w") as file, open(filename_1, "w") as file1, open(filename_2, "w") as file2:
        lines = text.splitlines()
        file.write(text)
        file1.write(lines[0])
        file2.write(lines[1])
    print(f"Розмір: {os.path.getsize(filename)}")


if __name__ == "__main__":
    main()
