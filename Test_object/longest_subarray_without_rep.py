
def func(s):  # longest_substring without repeating characters
    set_check = set()
    l = 0
    result = 0
    for r in range(len(s)):
        while s[r] in set_check:
            set_check.remove(s[l])
            l += 1
        set_check.add(s[r])
        result = max(result, r - l + 1)
    return result


def main():
    y = "batlab"
    result = func(y)
    print(result)


if __name__ == '__main__':
    main()
