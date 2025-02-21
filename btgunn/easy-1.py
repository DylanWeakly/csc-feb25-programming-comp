

text = "Hello World"

cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ''

for c in text:
    if c in cap:
        res += c.lower()
    else:
        res += c.upper()


print(res)