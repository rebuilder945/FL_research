lst=eval(input())
zero=[]
for i in lst:
    if i==0:
        lst.remove(0)
        zero.append(0)
    else:
        pass
newlist=lst+zero
print(newlist)
