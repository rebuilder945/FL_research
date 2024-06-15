lst=eval(input())
lst1=[]
for i in range(len(lst)):
    lst1.append(lst[i])
    a=lst1[0]
    lst.remove(a)
    if a not in lst:
        lst.insert(i,a)
    else:
        lst.insert(i,'nb啊')
    lst1.pop()
for i in range(len(lst)):
    if "nb啊" in lst:
        lst.remove('nb啊')
    else:
        break
print(lst)

