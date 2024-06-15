lst=eval(input())
lst.reverse()
lst1=[]
for i in range(len(lst)):
    x=lst[i]
    if x not in lst1:
        lst1.append(x)
lst1.reverse()
print(lst1)
