def i_like_characters(n):
    this_thing = "haha, I laugh."
    more = ""
    for char in this_thing:
        for i in range(n):
            more = more + char
    return more

print(i_like_characters(4))