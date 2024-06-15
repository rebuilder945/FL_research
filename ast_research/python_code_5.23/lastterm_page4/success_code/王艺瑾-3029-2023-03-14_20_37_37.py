a=input().split(",")
b=eval(input())
a=list(a)
c=()
d=[]
for i in range(len(a)):
    c=(a[i],b[i])
    d.append(list(c))
print(d)
