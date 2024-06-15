p=eval(input())
for i in range(len(p.copy())):
    l=max(p)
    if l==0:
        print(l,end='')
        if (p.copy()).count(l)<len(p.copy()) and len(p.copy())==(p.copy()).count(l):
            break
        else:
            continue
    else:
        print(l,end='')
        p.remove(l)
