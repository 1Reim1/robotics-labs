def main():
    arr = [1, 2, 3, 4, [5, 6], 7, 8]
    # arr = [1, 2, 3, 4, 7, 8]
    for item in arr:
        if type(item) == list:
            print("Exists")
            break
    else:
        print("Does not exists")


if __name__ == "__main__":
    main()
