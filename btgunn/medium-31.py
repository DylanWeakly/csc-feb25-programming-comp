value = -1234
val_str = str(value)[::-1]

neg = '-' in val_str

result = ''

if neg:
    result = '-' + val_str.replace('-', '')

print(result)