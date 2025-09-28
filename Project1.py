try:
    email = input("Enter your email: ")

    index = email.index("@")

    username = email[:index]
    domain = email[email.index("@") + 1:]

    print(f"Your username is '{username}' and your domain is '{domain}'")
    
except ValueError:
    print("Invalid email format. Please include an '@' symbol.")
