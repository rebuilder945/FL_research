n=eval(input())
list=[x for x in range(1,n+1)]
for i in list:
    if i==n:
        list.insert(0,n)
    else:
        continue
print(list)
