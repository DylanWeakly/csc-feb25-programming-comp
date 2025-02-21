rev = ""
sentence = "Hello World"
for word in sentence.split(" "):
    rev = word + " " + rev
print(rev.swapcase())