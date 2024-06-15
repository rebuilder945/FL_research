a=input().split(",")
b=input().split(",")
c=[]
for i in b:
    i=eval(i)
    c.append(i)
dic={}
d=[]
for i in range(len(a)):
    dic[a[i]]=c[i]
for k,v in dic.items():
    d.append([k,v])
d.sort(key=lambda x:x[1])
print(d)
