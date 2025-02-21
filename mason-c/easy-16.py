def sucker():
    arr = [1,3,10,15,18,4,8]
    new_arr = []
    for i in arr:
        if i % 3 == 0:
            if i % 5 == 0:
                new_arr.append("BethelSucks")
            else:
                new_arr.append("Bethel")
        elif i % 5 == 0:
            new_arr.append("Sucks")
        else:
            new_arr.append(i)
    return new_arr

print(sucker())