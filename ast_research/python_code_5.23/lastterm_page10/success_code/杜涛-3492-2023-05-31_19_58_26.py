a=input()
lst=list(a)
if a!='':
    b=[]
    for i in lst:
        if lst.count(i)==1:
            b.append(i)
    print(b[0])
else:
    print('None')

 
