a=input().split(",")
g =eval(input())
lst=[]
for i in range(len(a)):
    b=[a[i]+g[i]]
    lst.append(b)
print(lst)     
