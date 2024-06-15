n=eval(input())
list1=[]
for i in range(n+10):
    if i==0:
        list1.append(1)
    elif i==1:
        list1.append(1)
    else:
        new=list1[i-1]+list1[i-2]
        list1.append(new)
sum=0
list1.remove(1)
for i in range(n):
    item=list1[i+1]/list1[i]
    sum=sum+item
print("%.4f"%(sum))
