a=list(input().split(' '))
b={}
s=0
for x in a:
    b[x]=b.get(x,0)+1
    if b[x]>s:
        s=b[x]
list=[]
for f,v in b.items():
    if v==s:
        list.append([f,v])
list.sort()
for i in list:
    if i[1]==s:
        print(i[0],i[1])
