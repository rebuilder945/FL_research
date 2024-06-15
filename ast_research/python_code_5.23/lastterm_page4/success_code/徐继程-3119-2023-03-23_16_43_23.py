lst=eval(input())
lst1=[]
for i in range(len(lst)):
    a=lst[i]
    lst.pop(a)
    if a not in lst:
        lst.insert(i,a)
    else:
        lst.insert(i,'nb啊')
print(lst)

