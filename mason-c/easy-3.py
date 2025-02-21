def very_nice(arr):
    total = 0
    new_arr = []
    for i in arr:
        total += i
        new_arr.append(total)
    return new_arr

things = [1,3,10]
print(very_nice(things))