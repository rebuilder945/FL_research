l = input().split(",")
l=list(map(int,l))
n,m = eval(input())
if n >= 0:
    if n <len(l):
        for i in range(m):
            l.append(l[n])
        print(l)
    else:
        print("error")
if n <0:
    if n>=0-len(l):
        for i in range(m):
            l.append(l[n])
        print(l)
    else:
        print("error")
