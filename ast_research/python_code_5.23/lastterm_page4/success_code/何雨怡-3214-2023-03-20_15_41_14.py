lst=eval(input())
lst2=lst.copy()
zero=[]
for i in lst2:
    if i==0:
        lst.remove(0)
        zero.append(0)
    else:
        pass
newlist=lst+zero
print(newlist)
