def f_l():
    arr = [1,2,3,4,5]
    length = len(arr)
    first = arr[0]
    last = arr[length-1]
    new = []
    for i in arr:
        if i == first:
            new.append(last)
        elif i == last:
            new.append(first)
        else:
            new.append(i)
    return new

print(f_l())