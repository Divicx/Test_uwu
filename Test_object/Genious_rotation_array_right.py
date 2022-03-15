import math


def rotator(left, right):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

def shift_right(nums, k):  # my silly code
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    rotator(0, len(nums)-1)
    rotator(0, k - 1)
    rotator(k, len(nums) - 1)

def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    shift_right(nums, k)
    print(nums)


if __name__ == '__main__':
    main()
