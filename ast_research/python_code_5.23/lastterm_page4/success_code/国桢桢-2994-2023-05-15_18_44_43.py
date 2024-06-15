l = input().split()
n,m = eval(input())
if n >=0:
    if n<len(l):
        for i in range(m):
            l.append(l[n])
    else:
        print("error")
else:
    if n>=(-len(l)):
        for i in range(m):
            l.append(l[n])
        else:
            print("error")
