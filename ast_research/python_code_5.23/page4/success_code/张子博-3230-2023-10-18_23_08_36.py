p=eval(input())
for i in range(len(p)):
    l=max(p)
    if l==0:
        print(l,end='')
        break
    else:
        print(l,end='')
        p.remove(l)
