ls_str = input()
n1, n2 = map(int, input().split(","))

try:
    ls = list(map(int, ls_str.split()))
    if n1 in ls and n2 in ls:
        a = ls.index(n1)
        b = ls.index(n2)
        if a > b:
            a, b = b, a
        for i in range(b-a-1):
            del ls[a+1]
        print(ls)
    else:
        print("error")
except ValueError:
    print("error")
