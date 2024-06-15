name=input().split(",")
g =eval(input())
lst=[]
for i in range(len(name)):
    b=[name[i]+g[i]]
    lst.append(b)
print(lst)     
