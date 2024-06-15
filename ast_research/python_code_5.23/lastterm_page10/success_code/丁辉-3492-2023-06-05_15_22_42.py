st=input()
if st=='':
    print("None")
else:
    lst=list(st)
    a=[]
    for x in lst:
        if lst.count(x)==1:
            a.append(x)
print(a[0])
