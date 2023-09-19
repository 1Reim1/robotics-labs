def main():
    arr = [1, 2, 3, 1, 2, 3, 4, 5, 5]
    res = [i for n, i in enumerate(arr) if i not in arr[:n]]
    print(res)


if __name__ == "__main__":
    main()
