# Johnathan Fester Easy 3

def main():
    nlist = []
    list = [1,2,3,4,5,6,7,8,9,10]

    for i in range(len(list)):
        if i == 0:
            nlist.append(list[i])
        else:
            nlist.append(list[i] + list[i - 1])

    print(nlist)

if __name__ == '__main__':
    main()