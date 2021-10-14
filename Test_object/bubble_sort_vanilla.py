import random
import math


def sort_bubble(arr):
    pass


def intialize_arr():
    pass


def intialize_arr():  # could be improved by allowing user's input
    n = int(input("size of an array: "))
    array = [0] * n
    for element in range(n):
        array[element] = 1 + math.ceil(random.random() * 100)
    return array


def sort_bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    array = intialize_arr()
    print(array)
    result = sort_bubble(array)
    print(result)


if __name__ == '__main__':
    main()


