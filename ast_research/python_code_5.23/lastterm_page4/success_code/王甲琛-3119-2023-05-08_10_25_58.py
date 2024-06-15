lst=eval(input())
lst2=[]
for i in range(len(lst)):
    a=lst.pop(-1)
    if a not in lst2:
        lst2.append(a)
print(lst2.reverse())
