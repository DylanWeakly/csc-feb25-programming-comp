def func(l1):
    total = 0
    final = []
    for item in l1:
        final.append(int(item) + total)
        total = total + item
    return final


def main():
    print(func([1,2,3]))
    return


if __name__=="__main__":
    main()
