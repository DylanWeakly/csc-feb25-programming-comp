def mergerer(a, b):
    x = []
    i = 0
    while i < len(a) or i < len(b):
        if i < len(a):
            x.append(a[i])
        if i < len(b):
            x.append(b[i])
        i+=1
    return x

a = ["Dylan", "a", "and"]
b = ["is", "Dylan", "cool"]

print(mergerer(a,b))