def func(smth):
    binary_string = ''
    while smth > 0:
        binary_string = str(smth % 2) + binary_string
        smth //= 2

    # Handle the case when num is 0
    binary_result = binary_string if binary_string else '0'
    return binary_result


def main():
    print(func(11))
    return


if __name__=="__main__":
    main()
