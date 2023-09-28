import re

email = input("Enter your email : \n")

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

res = re.match(email_pattern, email)

if res:
    print("This is a valid email address")

else:
    print("Enter valid email address")