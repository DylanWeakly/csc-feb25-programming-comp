def func(smth):
    n = len(smth)
    for i in range(n):
        count = 0
        for j in range(n):
            if smth[i] == smth[j]:
                count += 1
        if count > n // 2:
            return smth[i]
    return -1


def main():
    print(func([3, 3, 4, 2, 3, 3, 3]))
    return


if __name__=="__main__":
    main()
