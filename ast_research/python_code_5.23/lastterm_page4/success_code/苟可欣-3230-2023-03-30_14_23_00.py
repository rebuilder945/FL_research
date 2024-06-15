ls=eval(input())
ls.sort(reverse=True)
for x in range(len(ls)):
    if max(ls)==0:
        print(0)
    else:
        a=ls[x]
        print(a,end='')
