text = 'hello world'
result = ''

vow = 'aeiouy'

for c in text:
    if c not in vow:
        result += c

print(result)