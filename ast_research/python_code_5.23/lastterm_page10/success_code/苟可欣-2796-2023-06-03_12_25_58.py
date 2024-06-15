a=input()
ls=[]
ls1=[]
for x in a:
    if x.isdigit():
        ls1.append(x)
    else:
        if ls1==[]:
            continue
        else:
            ls.append(ls1.copy())
            ls1.clear()
if ls1!=[]:
    ls.append(ls1)
s=[]
if ls==[]:
    print("No digits")
else:
    for x in ls:
        s.append(len(x))
    k=max(s)
    for x in ls[::-1]:
        if len(x)==k:
            print(''.join(x))
            break
