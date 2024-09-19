import hashlib

'''
Prelim Exam IAS - LAB

Baronia, James Scott N.
Binalla, Carmela

'''

user_input = input("Input your password: ")

h = hashlib.new("SHA256")
h.update(user_input.encode())

hashed = h.hexdigest()

print(f"Your password {user_input} is hashed to {hashed}.")





