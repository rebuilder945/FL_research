a=input().split(",")
g =eval(input())
lst=[]
for i in range(len(a)):
    b=[str(i) for i in a]
    c=b+g[i]
    lst.append(b)
print(lst)     
