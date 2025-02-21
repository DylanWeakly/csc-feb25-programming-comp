def func(smth):
    final = ""
    for char in smth:
        if not is_vowel(char):
            final = final + char
    
    return final

def is_vowel(char):
    if char.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

def main():
    print(func("some string"))
    return


if __name__=="__main__":
    main()
