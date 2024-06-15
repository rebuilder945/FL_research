lst=eval(input())
zero=[]
for i in range(len(lst)):
    if lst[i]==0:
        lst.pop(lst[i])
        zero.append(0)
    else:
        pass
newlist=lst+zero
print(newlist)
