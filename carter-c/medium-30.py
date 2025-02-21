def func(smth):
    n = len(smth)
    final = [-1] * n  
    for i in range(n):
        for j in range(i + 1, n):
            if smth[j] > smth[i]:
                final[i] = smth[j]
                break
    return final


def main():
    print(func([4, 5, 2, 10]))
    return


if __name__=="__main__":
    main()
