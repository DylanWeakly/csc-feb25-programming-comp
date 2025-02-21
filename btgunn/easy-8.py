values = [10, 3, 5, 20]

most = 0
most_f = 0
most_s = 0

for i in range(len(values)):
    for j in range(len(values)):
        first = values[i]
        second = values[j]

        result = first - second

        if result > most:
            most = result
            most_f = first
            most_l = second

print(f'({most_f} - {most_l})')

