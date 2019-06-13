import hashlib
m = hashlib.md5()
text = "aa".encode()
t = hashlib.md5(text).hexdigest()
print(t)
