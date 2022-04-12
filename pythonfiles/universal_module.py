def checkIfNotNumeric(*args):
    for x in args:
        if not (isinstance(x, (int, float))): #if x is not an integer or decimal
            return False
    return True


def addAllNumerics(*args):
    s = 0
    for x in args:
        s += x
    return s


myName = "Python Course"
