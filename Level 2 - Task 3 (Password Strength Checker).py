def upper(password):
    return any(ch.isupper() for ch in password)
def lower(password):
    return any(ch.islower() for ch in password)
def digit(password):
    return any(ch.isdigit() for ch in password)
def special(password):
    return any(ch in "!@#$%^&*(),.?\":{}|<>" for ch in password)

def check(password):
    if(len(password)>=8 and upper(password) and lower(password) and digit(password) and special(password)):
        return "Strong Password"
    else:
        return "Weak Password"
pwd = input("Enter your Password : ")
print(check(pwd))