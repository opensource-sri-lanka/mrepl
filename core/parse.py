def add(mathDef):
    out = 0
    b = mathDef.split("+")

    # parsing
    i = 0
    while i < len(b):
        out += int(b[i])
        i += 1
    return out


def substract(x, y):
    output = x - y
    return output


def multiply(x, y):
    output = x * y
    return output


def divide(x, y):
    output = x / y
    return output
