def fibonacci(n):
    a,b = 0,1
    sequence =[]
    for i in range(n):
        sequence.append(a)
        a,b = b,a+b
    return sequence
t= int(input("Enter the number of Terms : "))
print("Fibonacci Sequence : ",*fibonacci(t))