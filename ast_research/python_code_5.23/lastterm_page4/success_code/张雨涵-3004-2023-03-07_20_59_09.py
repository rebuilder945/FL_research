lst=eval(input())
lst1=[]
for i in lst:
    if i<2:
            continue
    else:
        for j in range(2,i):
            if i %j==0 :
                break
            else:
                lst1.append(i)
                break
print(lst1)
#break后面不会执行else
