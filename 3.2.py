def main():
    s1 = input()
    s2 = input()
    if len(s1) > len(s2):
        print("Перша стрічка довша")
    elif len(s1) < len(s2):
        print("Друга стрічка довша")
    else:
        print("Стрічки однакові за довжиною")
        if s1 == s2:
            print("Стрічки однакові за вмістом")
        else:
            print("Стрічки різні за вмістом")


if __name__ == "__main__":
    main()
