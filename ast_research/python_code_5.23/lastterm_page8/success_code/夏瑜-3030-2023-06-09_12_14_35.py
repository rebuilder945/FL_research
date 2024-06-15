n=list(input().split(','))
m=list(input().split(','))
d1={}
for i in range(len(n)):
    d1[n[i]]=int(m[i])
list=[]
for k,v in d1.items():
    list.append([k,v])
list.sort(key=lambda x:x[1])
print(list)
