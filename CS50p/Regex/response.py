import validators


email_input = str(input("What's your email adress? "))
if validators.email(email_input):
    print("Valid")
else:
    print("Invalid")
