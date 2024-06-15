ls = input().split()
n,m=eval(input())
if -len(ls)<=int(n)<=len(ls)-1:
    a=list[n]
    for x in range(m):
        ls.append(a)
else:
    print("error")
