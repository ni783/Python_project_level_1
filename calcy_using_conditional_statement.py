# Simple Calculator using conditional statements (if, elif, else)

num1 = int(input("Enter value 1: "))
num2 = int(input("Enter value 2: "))
opr = input("Enter operator (+, -, *, /): ")

if opr == "+":
    print("Result:", num1 + num2)
elif opr == "-":
    print("Result:", num1 - num2)
elif opr == "*":
    print("Result:", num1 * num2)
elif opr == "/":
    # Check for division by zero
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator! Please enter one of +, -, *, /.")

