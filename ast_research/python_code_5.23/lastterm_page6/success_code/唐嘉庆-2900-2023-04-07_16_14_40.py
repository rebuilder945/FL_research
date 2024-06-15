n=eval(input())
jack=[]
lst=[]
lst1=[]
if n==1 or n<0 or n%1 !=0:
    print('illegal input')
elif n==2:
    print(2)
else:
    for x in range(2,n):
        a=str(x)
        if a==a[::-1]:
            jack.append(x)
    for x in jack:
        for i in range(2,x):
            if int(x/i)==x/i:
                lst.append(x)
    for x in jack:
        if x not in lst:
            lst1.append(x)              
    d=' '.join(str(i) for i in lst1)
    print(d)
