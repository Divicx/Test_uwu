
import math

def func(n):  # is it a power of 3?
    if n <= 0:
        return False
    result = math.log10(n) / math.log10(3)
    if math.modf(result)[0] != 0:
        return False
    return True

def main():
    n = -3
    result = func(n)
    print(result)


if __name__ == '__main__':
    main()
