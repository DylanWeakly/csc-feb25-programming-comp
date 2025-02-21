def check(text):
    current_open = 0
    b_open = 0
    b_close = 0

    for c in text:
        if c == '(':
            b_open += 1
        elif c == ')':
            b_close += 1
        
        if b_close > b_open:
            return False
    
    return b_open == b_close


print(check('(())'))
print(check('(()'))