a=input().split(",")
b=input().split(",")
c=[x for x in b]
lst=[]
for i in range(len(a)):
    lst.append([a[i],c[i]])
lst.sort(key=lambda x:x[1],reverse=False)
print(lst)
