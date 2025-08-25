def calculator(a,b,operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        if b!=0:
            return a/b
        else:
            return "Division by zero not possible."
    elif operator == '%':
        if b!=0:
            return a%b
        else:
            return "Division by zero not possible."
    else:
        return "Invalid Operator."
    
num1 = float(input("Enter the First Number : "))
num2 = float(input("Enter the Second Number : "))
op = input("Enter Operator : ")
print("Result : ",calculator(num1,num2,op))