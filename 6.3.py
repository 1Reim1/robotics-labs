import pickle


def main():
    filenames = [r"6\file.txt", r"6\first.txt", r"6\second.txt"]
    contents = {}
    for filename in filenames:
        with open(filename) as file:
            contents[filename] = file.read()
    print(contents)
    with open(r"6\dict.pkl", "wb") as file:
        pickle.dump(contents, file)


if __name__ == "__main__":
    main()
