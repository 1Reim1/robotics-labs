def main():
    s1 = input()
    s2 = input()
    if len(s1) > len(s2):
        print("The first string is longer")
    elif len(s1) < len(s2):
        print("The second string is longer")
    else:
        print("The strings are the same length")
        if s1 == s2:
            print("The strings are identical in content")
        else:
            print("The strings are different in content")


if __name__ == "__main__":
    main()
