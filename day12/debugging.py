def add(n1, n2):
    try:
        print(n1 + n2)
    except TypeError:
        print("You have entered different operand types, cannot add integer and string, convert one of them first")

    print("I have moved")


add(4, 'five')
