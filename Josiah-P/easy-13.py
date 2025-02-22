import random
def hello():
    p = [1,2,3,4,5,6,7,8,9]
    counter=0
    for i in p:
        print(i)
        if i%2 !=0:
            counter+=i
    print(counter)
hello()