values = [1, 2, 3, 4, 5, 6]

n = 2

start = values[:n]
end = values[n::]
end.reverse()
start.extend(end)
print(start)