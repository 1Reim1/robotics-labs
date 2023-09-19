def main():
    arr = ['a', 'b', 'b', 'c', 'a', 'd', 'a']
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    print(freq)


if __name__ == "__main__":
    main()
