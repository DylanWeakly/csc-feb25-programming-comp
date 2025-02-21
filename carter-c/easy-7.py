def func(smth):
    final = ""
    index = 0
    for thing in smth:
        if index % 2 == 0:
            final = final + thing.lower()
        else:
            final = final + thing.upper()
        index += 1
    return final


def main():
    print(func("HelloWorld"))
    return


if __name__=="__main__":
    main()
