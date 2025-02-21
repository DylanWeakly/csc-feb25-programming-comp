from math import factorial

def func(smth):
    for i in range(smth):
        for j in range(smth-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()


def main():
    print(func(11))
    return


if __name__=="__main__":
    main()
