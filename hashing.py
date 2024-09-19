import hashlib

'''
Prelim Exam IAS - LAB

Baronia, James Scott N.
Binalla, Carmela

'''

h = hashlib.new("SHA256")
h.update(b"Hello World")

print(h.hexdigest())

