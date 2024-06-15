lst=eval(input())
lst1=[]
for i in lst:
    if i>=2:
        for j in range(2,i,1):
            if i%j == 0:
                break
        else:
            lst1.append(i)
print(lst1)
