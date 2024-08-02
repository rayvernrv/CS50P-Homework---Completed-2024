from validator_collection import validators, errors


try:
    email_address = validators.email(input("Email: "))
    print("Valid")

except errors.InvalidEmailError:
    print("Invalid")

except errors.EmptyValueError:
    print("No email was input")
