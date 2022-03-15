def func(n):  # is it a power of 3?
    if n == 3:
        return True
    if n == 1:
        return True
    if n % 3 == 0 and n != 0:
        return func(n // 3)
    else:
        return False

def main():
    n = 0
    result = func(n)
    print(result)


if __name__ == '__main__':
    main()