# Johnathan Fester Easy 4

def main():

    s = input('Enter a string: ')
    n = ''

    for i in range(len(s)):
        for j in range(3):
            n = n + str(s[i])

    print(n)

if __name__ == '__main__':
    main()