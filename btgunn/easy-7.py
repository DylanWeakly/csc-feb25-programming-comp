text = 'hello'
result = ''

for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].upper()
    else:
        result += text[i].lower()

print(result)