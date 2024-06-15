lst=eval(input())
lst1=[]
for i in lst:
    if i==1 or i==2:
            lst1.append(i)
    else:
        for j in range(2,i):
            if i %j==0 :
                break
            else:
                lst1.append(i)
                break
print(lst1)
#什么时候加break，什么时候不加
