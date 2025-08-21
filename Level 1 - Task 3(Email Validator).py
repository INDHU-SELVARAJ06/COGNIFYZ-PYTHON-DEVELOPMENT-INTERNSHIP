def valid_email(e):
    if "@" not in e:
        return False
    
    parts =e.split("@")
    if len(parts)!=2:
        return False
    
    username,domain = parts
    if username =="" or domain=="":
        return False
    
    if "." not in domain:
        return False
    
    if domain.startswith(".") or domain.endswith("."):
        return False
    
    else:
        return True

a=input("Enter Email Address : ")    
if valid_email(a):
    print("The Given Email Address is Valid")
else:
    print("The Given Email Address is InValid")
