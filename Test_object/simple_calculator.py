
def calc(num1, num2, ops):
    if ops == "+":
        return num1 + num2
    elif ops == "-":
        return num1 - num2
    elif ops == "*":
        return num1 * num2
    elif ops == "/":
        return num1 / num2
    else:
        print("Invalid operator")


number_1 = float(input("enter a first number: "))
op = input("enter operator: ")
number_2 = float(input("enter a second number: "))

result = calc(number_1, number_2, op)
print("Result of calculation: " + str(result))
