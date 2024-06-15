lst=eval(input())
lst1=[]
for x in lst:
    if x>=2:
        for i in range(2,x,1):
            if x%i==0:
                break
        else:
            lst1.append(x)
print(lst1)
