
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err_0:
    print(err_0)
except ValueError:
    print("Invalid input")
