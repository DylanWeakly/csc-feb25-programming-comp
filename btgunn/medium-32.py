text = "aabcccccaaa"
text += ' '

cur_letter = text[0]
cur_num = 0

result = ''

for c in text:
    if c != cur_letter:
        result += cur_letter + str(cur_num)
        cur_letter = ''
        cur_num = 0

    cur_letter = c
    cur_num += 1


print(result)