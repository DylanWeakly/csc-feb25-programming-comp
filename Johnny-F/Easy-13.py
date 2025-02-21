# Johnathan Fester Easy 13

def main():

    list = [1,2,3,4,5,6,7,8,9]
    sum_odd = 0

    for i in range(len(list)):
        if list[i] % 2 != 0:
            sum_odd += list[i]

    print(sum_odd)

if __name__ == '__main__':
    main()