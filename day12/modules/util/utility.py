def mult(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("You have passed 0 as the param, cannot divide by zero")
    try:
        return n1 / n2
    except TypeError:
        raise ValueError("Don't pass a string buddy")


print(__name__)


def add(n1, n2, op='add'):
    try:
        if(op == 'divide'):
            return n1 / n2
        else:
            return n1 + n2
    except ValueError as err:
        return err
    except OSError as err:
        return err