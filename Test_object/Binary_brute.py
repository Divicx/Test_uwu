
def input_array(size, arr):
    pass


def find_value_brut(val, arr):
    pass


def find_value_bi(val,arr, mid):
    pass


def test_location(val, arr, mid):
    pass


def main():
    size_of_array = int(input("how big is array: ")) # all this can be one line actually
    array = [0] * size_of_array #
    input_array(size_of_array, array) #
    print("original array: " + str(array))
    value = int(input("Wanted Value: "))
    result_brute, result_bi = find_value_brut(value, array), find_value_bi(value, array)
    print("resulting position (brute): " + str(result_brute))
    print("resulting position (binary): " + str(result_bi))


def input_array(size, arr):
    if size < 12:
        for pos in range(size):
            arr[pos] = input()
    else:
        for pos in range(size):
            arr[pos] = pos
    return arr


def test_location(val, arr, mid):
    mid_value = int(arr[mid])

    if mid_value == val:
        if mid - 1 >= 0 and int(arr[mid - 1]) == val:
            return "Left"
        else:
            print(" Huh?")
            return "Done"
    elif mid_value > val:
        return "Left"
    elif mid_value < val:
        return "Right"


def find_value_bi(val, arr):
    low_end, hi_end = 0, len(arr) - 1
    while low_end <= hi_end:
        mid = (low_end + hi_end) // 2
        print("lo:", low_end, ", hi:", hi_end, ", mid:", mid, ", mid_number:", arr[mid])

        result = test_location(val, arr, mid)                                    #location helper

        if result == "Done":
            return mid
        elif result == "Left":
            hi_end = mid - 1
        elif result == "Right":
            low_end = mid + 1
    return 'inf'


def find_value_brut(val, arr):
    for pos in range(len(arr)):
        if val == int(arr[pos]):
            return pos
    return 'inf'


if __name__ == '__main__':
    main()
