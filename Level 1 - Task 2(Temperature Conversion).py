def celsius_to_fahrenheit(c):
    return (c*9/5)+32
def fahrenheit_to_celsius(f):
    return (f-32)*5/9

t = float(input("Enter the Temperature : "))
u = input("Is the Unit C or F ? ")

if u == 'C' or u=='c':
    print("Converted Temperature in Fahrenheit is : %.2f F" % celsius_to_fahrenheit(t))
elif u=='F' or u=='f':
    print("Converted Temperature in Celsius is : %.2f C" % fahrenheit_to_celsius(t))
else:
    print("Invalid.")