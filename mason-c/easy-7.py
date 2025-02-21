def flipThings(things):
    count=1
    sent = ""
    for char in things:
        if count % 2 == 0:
            sent = sent + char.upper()
        else:
            sent = sent + char.lower()
        count += 1
    return sent
sentences = 'This is stressful'
print(flipThings(sentences))