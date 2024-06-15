lst=eval(input())
lst1=[]
for i in lst:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lst1.append(i)
print(lst1)
