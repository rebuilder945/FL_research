ls=[4,3,2,3,4]
lst=[]
for i in ls:
    if lst.count(i) < 1:
        lst.append(i)
    lst.sort()
print(lst)
