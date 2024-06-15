lst=eval(input())
lst1=[]
for i in lst:
    if i==2 or i==3:
        lst1.append(i)
    if i>=4:
        for j in range(2,i//2+1):
            if i%j==0:
                break
            lst1.append(i)
print(lst1)
