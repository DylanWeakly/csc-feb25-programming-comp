def func(l1, l2):
    length = len(l1)
    final = []
    for i in range(0,length):
        final.append(l1[i])
        final.append(l2[i])
    
    
    return final


def main():
    print(func([1,3,5,7],[2,4,6,8]))
    return


if __name__=="__main__":
    main()
