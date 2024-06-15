def bcf(n,m):
    lst=[]
    ls=[]
    for i in range(n,m):
        lst.append(str(i))
    for s in lst:
        for l in lst:
            for p in lst:
                if len(s+l+p)<=3 and eval(s)!=0 and s not in [l,p] and l not in [s,p]:
                    ls.append(s+l+p)
    return ls
s=input().split()
try:
    n=eval(s[0])
    m=eval(s[1])
    if n>=m or n<0 or m<0 or m-n<3 or type(n) is float or type(m) is float:
        print('illegal input')
    else:
        print(' '.join(bcf(n,m)))
except:
    print('illegal input')
