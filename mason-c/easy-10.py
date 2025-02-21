def prod():
    nums = [2,4,5]
    yes = 1
    for i in nums:
        yes *= i
    return yes

print(prod())