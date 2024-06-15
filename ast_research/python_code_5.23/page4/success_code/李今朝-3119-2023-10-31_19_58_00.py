lst=eval(input())
lst.reverse()
lst2=[]
for x in lst:
    if x not in lst2:
        lst2.append(x)
lst2.reverse()
print(lst2)
