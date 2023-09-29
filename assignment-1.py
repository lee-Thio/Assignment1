#Lee Thiong'o 
#SCT211-0536/2022

operator = input("enter operator:")
num1 =int(input("enter the first number:"))
num2 =int(input("enter the second number: "))
#addition
if operator == '+':
    print("sum = ",num1 + num2)

#subtraction 
elif operator == '-':
    print("difference = ",num1 - num2)

#multiplication
elif operator == '*':
    print("product = ",num1 * num2)

#division
elif operator == '/':
    print("division = : ",num1 / num2)

else:
    print("invalid operator")