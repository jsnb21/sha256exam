import hashlib

'''
Prelim Exam IAS - LAB

Baronia, James Scott N.
Binalla, Carmela

'''

user_input = input("Input your password: ")

h = hashlib.new("SHA256")
h.update(user_input.encode())

hashed_password = h.hexdigest()

print(f"Your password {user_input} is hashed to {hashed_password}.")


checked_login = input("Input your password again: ")

h2 = hashlib.new("SHA256")

h2.update(checked_login.encode())

login_hash = h2.hexdigest()

if login_hash == hashed_password:
    print("You've been signed in.")
else: 
    print("Incorrect password.")




