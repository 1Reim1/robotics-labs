from itertools import permutations


def main():
    arr = [1, 2, 3]
    for p in permutations(arr):
        print(p)


if __name__ == "__main__":
    main()
