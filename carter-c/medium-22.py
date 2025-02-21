def func(smth):
    a = {}
    for thing in smth:
        s = ''.join(sorted(thing))
        if s in a:
            a[s].append(thing)
        else:
            a[s] = [thing]

    final = list(a.values())

    return final


def main():
    print(func(["bat", "tab", "cat", "tac", "act"]))
    return


if __name__=="__main__":
    main()
