# Johnathan Fester Easy 10

def main():

    list = [2, 3, 4, 9, 7, 5]
    product = list[0]

    for i in range(len(list)-1):
        product = product * list[i+1]

    print(product)

if __name__ == '__main__':
    main()


