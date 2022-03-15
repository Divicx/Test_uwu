
import math

def func(nums):  # 3 sum 0
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res

def main():
    y = [2, 1, 0, -2, -1]
    result = func(y)
    print(result)


if __name__ == '__main__':
    main()
