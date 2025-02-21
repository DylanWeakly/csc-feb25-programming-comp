def func(smth, n):
    res = []
    while smth:
        num = smth.pop()
        diff = n - num
        if diff in smth:
            res.append((diff, num))
         
    res.reverse()
    return res


def main():
    print(func([1, 2, 3, 4, 5], 6))
    return


if __name__=="__main__":
    main()
