while True:
    a=input() or 'q'
    b=[]
    c={}
    if a!='q':
        b.append(a)
        for x in b:
            c[x]=c.get(x,0)+1
        lst=list(c.items())
        lst.sort(key=lambda x:x[1],reverse=True)
        print(lst[0][0],lst[0[1]])
    else:
        break
