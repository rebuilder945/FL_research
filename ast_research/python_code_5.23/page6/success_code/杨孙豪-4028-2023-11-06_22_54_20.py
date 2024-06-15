n=eval(input())
if n<0 or n-n//1!=0:
    print('illegal input')
else:
    lst=[x for x in range(2,n)]
    if 0 in lst:
        lst.remove(0)
    if 1 in lst:
        lst.remove(1)
    result=[]
    for i in lst[:]:
        for m in range(2,i):
            if i%m!=0:
                continue
            elif i in lst:
                lst.remove(i)

    cst=[]
    for i in lst:
        x=str(i)
        b=x[::-1]
        if x==b:
            cst.append(i)

    bst=list(map(str,cst))
    a=' '.join(bst)
    print(a)
