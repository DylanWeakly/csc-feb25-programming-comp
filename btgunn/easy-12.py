text = "swiss"

chars = dict()

for c in text:
    if c in chars:
        chars[c] += 1
    else:
        chars[c] = 1


for key, value in chars.items():
    if value == 1:
        print(key)
        exit()