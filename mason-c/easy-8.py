def max_dist():
    arr = [10,11,5,20]
    mini = arr[0]
    maxi = arr[0]
    for i in arr:
        if i < mini:
            mini = i
        if i > maxi:
            maxi = i
    distance = maxi - mini
    return distance

print(max_dist())