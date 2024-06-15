lst=eval(input())
lst2=[]
for i in lst:
    if i==0:
        lst.remove(i)
        lst2.append(i)
    else:
        pass
lst3=lst+lst2
print(lst3)
