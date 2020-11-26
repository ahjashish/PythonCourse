# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from day12.modules.util import dummy


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm, Welcome to Python!')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def simple_calculate(a, b):
    print(f"The result of multiply is { dummy.mult(a, b)}")
    print(f"The result of divide is { dummy.divide(a, b)}")


def sci_calculate(a, b):
    print(f"The result of sci multiply is { dummy.mult(a, b)}")
    print(f"The result of sci divide is { dummy.divide(a, b)}")


simple_calculate(2, 2)
sci_calculate(2, 2)
