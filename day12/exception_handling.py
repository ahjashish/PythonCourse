while True:
    try:
        age = int(input("Enter your age: "))
        age_in_dogs_year = 10 / age

    except ZeroDivisionError:
        print("enter age greater than 0")
        continue

    except ValueError:
        print("Please enter a no.")
        break

    except ValueError:
        print("!!!!")

    else:
        print(f"thank you, and your age is {age}")
        break

    finally:
        print("I will always get printed no matter what :)")

    print("can you hear me??????")


def division_fn(num1, num2):
    try:
        return num1/num2
    except (ZeroDivisionError, TypeError) as err:
        print(f'error: {err}')

print(division_fn(1,'0'))
print(division_fn(1,0))
print(division_fn(1,4))


print("Hello!!!!")
# raise TypeError("yo")
raise Exception("Any message ")
print("bye")



try:
    age = int(input("age: "))
    age = 10/age
    raise ValueError("Ending the program")
    # raise Exception("quit")

except ValueError:
    print("Please enter a no.")

    #
    # Try block for handling exception
    #     Exception -> Error
    #         How do you know it is an error, what are errors?