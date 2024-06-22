while True:
    operator = input("Please enter an operator (+, -, *, /): ")
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        break
    else:
        print("Invalid operator, please enter an operator")


num1 = float(input("enter the first number "))
num2 = float(input("enter the first number "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} not found ! ")


  
