import hashlib

s = "Python Bootcamp"
s_hashed = hashlib.sha1(s.encode())

print(f'String before hashing: "{s}"')
print(f'String after hashing: "{s_hashed.hexdigest()}"')