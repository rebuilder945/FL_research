n=eval(input())
list1=[0,1,1]
list2=[]
for i in range(n):
    y=list1[i]+list1[i+1]
    x=list1[i+1]+list1[i+2]
    list1.append(x)
    m=x/y
    list2.append(m)
a=sum(list2)
print("%.4f"%(a))
