import pickle


def main():
    filenames = [r"folder\file.txt", r"folder\first.txt", r"folder\second.txt"]
    contents = {}
    for filename in filenames:
        with open(filename) as file:
            contents[filename] = file.read()
    print(contents)
    with open(r"folder/dict.pkl", "wb") as file:
        pickle.dump(contents, file)


if __name__ == "__main__":
    main()
