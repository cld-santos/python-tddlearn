import sys


def sum_all(values):
    print("2nd", sys.getrefcount(first))
    result = 0
    for value in values:
        result += value
        print("3rd", sys.getrefcount(first))

    print("4th", sys.getrefcount(first))
    return result


first = [1, 2, 3]
print("1st", sys.getrefcount(first))

sum_all(first)

print("last", sys.getrefcount(first))