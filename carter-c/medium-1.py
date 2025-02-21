def func(smth):
    smth.sort()

    res = 1
    cnt = 1
    for i in range(1, len(smth)):
        if smth[i] == smth[i - 1]:
            continue
        if smth[i] == smth[i - 1] + 1:
            cnt += 1
        else:
            cnt = 1

        res = max(res, cnt)

    return res


def main():
    print(func([1,2,5,8,9,13]))
    return


if __name__=="__main__":
    main()
