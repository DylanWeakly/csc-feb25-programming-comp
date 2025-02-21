def brack(text):
    current_open = 0
    b_open = 0
    b_close = 0
    b2_open = 0
    b2_close = 0
    b3_open = 0
    b3_close = 0

    for c in text:
        if c == '(':
            b_open += 1
        elif c == ')':
            b_close += 1

        if c == '{':
            b2_open += 1
        elif c == '}':
            b2_close += 1

        if c == '[':
            b3_open += 1
        elif c == ']':
            b3_close += 1

        if b_close > b_open:
            return False
        if b2_close > b2_open:
            return False
        if b3_close > b3_open:
            return False

    return True

print(brack('{}[]])(()))()())[][][{{}'))
print(brack('[({}())()[()](()){()}]'))