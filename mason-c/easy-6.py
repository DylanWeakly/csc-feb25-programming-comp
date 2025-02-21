def uniqueness(smth):
    count = set()
    for element in smth:
        count.add(element)
    return len(list(count))

print(uniqueness([5,6,6,7,8,9,10,10]))