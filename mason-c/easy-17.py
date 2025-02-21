def reverser():
    smth = 12345
    reversed = ""
    for char in str(smth):
        reversed = char + reversed
    return int(reversed)
print(reverser())