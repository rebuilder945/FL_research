from re import L


m=input().split(",")
n=eval(input())
ls=[]
for i in range(len(m)):
    lt=[]
    lt.append(m[i])
    lt.append(n[i])
    ls.append(lt)
ls.sort(key=lambda lt:lt[1],reverse=False)
print(ls)
