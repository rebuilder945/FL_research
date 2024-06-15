def fibonacci(n):
    if n<=2:
        return 1
    a,b=1,1
    for x in range(3,n+1):
        v=a+b
        a,b=b,v
    return v
n=int(input())
list1=[]
for x in range(2,n+3):
    list1.append(fibonacci(x))
list2=[]
for i in range(0,len(list1)):
    if i+1<=len(list1)-1:
        x=(list1[i+1])/(list1[i])
        list2.append(x)
m=sum(list2[:n+1])
print("%.4f"%m)

    

