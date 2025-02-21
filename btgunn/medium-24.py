values = [3, 3, 4, 2, 3, 3, 3]

d = dict()

for v in values:
    if v in d:
        d[v] += 1
    else:
        d[v] = 1

most_key = None
most_val = 0

for key, value in d.items():

    if value > most_val:
        most_key = key
        most_val = value

print(most_key)