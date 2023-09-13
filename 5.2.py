from itertools import permutations


def main():
    arr = [1, 2, 3]
    for sub_list in permutations(arr):
        print(sub_list)


if __name__ == "__main__":
    main()
