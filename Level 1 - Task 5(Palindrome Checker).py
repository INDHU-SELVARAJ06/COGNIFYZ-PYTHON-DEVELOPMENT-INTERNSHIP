def palindrome(a):
    rev = a[::-1]
    if a == rev:
        return True
    else:
        return False
b= input("Enter a word:")
if palindrome(b):
    print(b, "is a Palindrome")
else:
    print(b, "is not a Palindrome")