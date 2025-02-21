# Johnathan Fester Easy 14

def main():
    list = [1,2,3,4,5,6,7,8,9]
    new_list = []

    new_list.append(list[len(list)-1])

    for i in range(len(list)-2):
        new_list.append(list[i + 1])

    new_list.append(list[0])

    print(new_list)

if __name__ == '__main__':
    main()