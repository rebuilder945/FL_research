lst=eval(input())
lst1=[]
for i in lst:
    if 0 in lst:
        lst1.append(0)
    if 1 in lst:
        lst1.append(1)
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lst1.append(i)
print(lst1)
