
def func(n):  # count primes up to n (not included)
    primes = [True for i in range(n)]
    i = 2
    while i * i < n:
        if primes[i]:
            for p in range(i * i, n, i):
                primes[p] = False
        i += 1

    counter = 0
    for i in range(2, len(primes)):
        if primes[i]:
            counter += 1
    return counter


def main():
    n = 15
    result = func(n)
    print(result)


if __name__ == '__main__':
    main()