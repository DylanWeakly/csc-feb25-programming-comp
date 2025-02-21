values = [1, 2, 3, 4]

first = values[0]
last = values[len(values) - 1]

values[0] = last
values[len(values) - 1] = first

print(values)