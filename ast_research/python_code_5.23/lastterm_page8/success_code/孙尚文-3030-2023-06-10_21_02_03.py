a=input().split(",")
b=input().split(",")
c=list(map(int,b))
d=dict(zip(a,c))
lst=[]
for k,v in d.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1])
print(lst)
