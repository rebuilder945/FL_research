n=eval(input())
list=[x for x in range(1,n+1)]
for i in list:
    if i==1:
        list.remove(1)
        list.append(1)
    else:
        continue
print(list)
