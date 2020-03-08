print("zero in operator placeholder will exit the programm")
while True:
    ops = input("Enter the operator: *, /, -, +, %, **: ")
    if ops == "0": break
    elif ops == "exit": break
    num1 = float(input("x = "))
    num2 = float(input("y = "))

    if ops == "+":
        print("x + y = ", num1 + num2)
    elif ops == "-":
        print("x - y = ", num1 - num2)
    elif ops == "*":
        print("x * y = ", num1 * num2)
    elif ops == "/":
        print("x / y = ", num1 / num2)
    elif ops == "**":
        print("x ** y = ", num1 ** num2)
    elif ops == "%":
        print("x % y = ", num1 % num2)
    else:
        print("invalid operator")