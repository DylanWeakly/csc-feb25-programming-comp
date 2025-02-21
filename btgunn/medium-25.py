values = [1, 2, 3, 4, 5]
target = 6

pairs = []

for i in range(len(values)):
    for j in range(len(values)):
        if i != j:
            if values[i] + values[j] == 6:

                found = False
                for p in pairs:
                    if p[0] == values[j] and p[1] == values[i]:
                        found = True

                if not found:
                    pairs.append((values[i], values[j]))


print(pairs)