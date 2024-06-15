n=eval(input())
a=range(1,n+1)
list1=[]
m=a[0]
for x in range(len(a)-1):
    list1.append(a[x+1])
list1.append(m)
print(list1)
