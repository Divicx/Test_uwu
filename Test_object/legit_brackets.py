
import math


def func(s):  # Brackets
    stack = []
    close_open = {")": "(", "]": "[", "}": "{"}
    for br in s:
        if br in close_open:
            if stack and stack[-1] == close_open[br]:
                stack.pop()
            else:
                return False
        else:
            stack.append(br)
    return True if not stack else False


def main():
    y = "()"
    result = func(y)
    print(result)


if __name__ == '__main__':
    main()
