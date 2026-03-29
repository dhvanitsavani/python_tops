import re

pattern = r"^\w+@\w+\.\w+\s*$"
email = input("Enter email : ")

if re.match(pattern, email):
    print("email is valid")
else:
    print("email is not valid")
