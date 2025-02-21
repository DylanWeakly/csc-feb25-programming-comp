def func(smth):
    final = set()
    for thing in smth:
        final.add(thing)
    
    return list(final)


def main():
    print(func([1,2,3,4,5,6,5,1,4]))
    return


if __name__=="__main__":
    main()
