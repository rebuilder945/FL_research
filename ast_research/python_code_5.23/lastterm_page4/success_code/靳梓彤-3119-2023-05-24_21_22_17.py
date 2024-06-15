lst=eval(input())
lst.reverse()
lst1=[]
for x in lst:
    if x not in lst1:
        lst1.append(x)
lst1.reverse()
print(lst1)
