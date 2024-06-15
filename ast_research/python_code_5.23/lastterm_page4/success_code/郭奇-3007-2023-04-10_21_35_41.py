ls = input()
n1,n2 = map(int,input().split(","))
if n1 in ls and n2 in ls:
    a = index(n1)
    b = index(n2)
    for i in range(n2-n1-1):
        del ls[i]
    print(ls)
else:
    print(error)
