def add(mathDef):
    b = mathDef.split("+")
    if len(b) == 0:
        return 0
    out = int(b[0])

    # parsing
    i = 1
    while i < len(b):
        out += int(b[i])
        i += 1
    return out


def substract(mathDef):
    b = mathDef.split("-")
    if len(b) == 0:
        return 0
    out = int(b[0])

    # parsing
    i = 1
    while i < len(b):
        out -= int(b[i])
        i += 1
    return out


def multiply(mathDef):
    b = mathDef.split("*")
    if len(b) == 0:
        return 0
    out = int(b[0])

    # parsing
    i = 1
    while i < len(b):
        out = out * int(b[i])
        i += 1
    return out


def divide(mathDef):
    b = mathDef.split("/")
    if len(b) == 0:
        return 0
    out = int(b[0])

    # parsing
    i = 1
    while i < len(b):
        out = out / int(b[i])
        i += 1
    return out
