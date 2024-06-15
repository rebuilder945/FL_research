def sum_list():
    ls = []
    while True:
        a = input()
        if a == '#':
            break
        else:
            ls.append(int(a))
    n = len(ls)
    s = sum(ls)
    print(n,s)
sum_list()
