lst=eval(input())
lst1=[]
for i in lst:
    if i == 2:
        lst1.append(i)
    elif i>2:
        for j in range(2,i):
            if i %j==0 :
                break
        else:
            lst1.append(i)
    else:
         continue
print(lst1)
# 注意，这里可以把else提前
