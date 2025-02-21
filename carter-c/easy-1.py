

def reverse_order_n_case(smth):
    reversed = ""
    words = smth.split()
    for word in words:
        flipped = ""
        for char in word:
            if char.isupper():
                flipped = flipped + char.lower()
            else:
                flipped = flipped + char.upper()
        reversed = flipped + " " + reversed
        
        
    return reversed


def main():
    print(reverse_order_n_case("Hello World"))
    return


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
