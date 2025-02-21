def func(smth, n):
    final = ""
    for char in smth:
        for i in range(n):
            final = final + char
    
    return final


def main():
    print(func("abc", 3))
    return


if __name__=="__main__":
    main()
