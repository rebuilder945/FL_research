lst=eval(input())
lst1=[]
for i in lst:
    for j in range(0,i):
        if i%j==0:
            break
    else:
        lst1.append(i)
print(lst1)
