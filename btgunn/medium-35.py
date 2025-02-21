text = 'a2b1c5a3'

cur_letter = ''

result = ''

for c in text:
    try:
        num = int(c)
        result += (cur_letter * num)
    except:
        cur_letter = c


print(result)