lst=eval(input())
lst2=[]
lst3=[]
for i in range(len(lst)):
    if lst[i]==0:
        lst2.append(0)
    else:
        lst3.append(lst[i])
print(lst3+lst2)

