a=input()
b={}
c=[]
d=''
for i in a:
    if i !=  ' ':
        d+=i
    else:
        if d in c:
            b[d]+=1
            d=''
        else:
            c.append(d)
            b[d]=1
            d=''
if d in c:
            b[d]+=1
else:
    c.append(d)
    b[d]=1
    d=''
e=[]
for k,v in b.items():
    e.append([k,v])
e.sort(key=lambda x:x[0],reverse=True)
e.sort(key=lambda x:x[1],reverse=True)
print(e[0][0],e[0][1])
for i in range(1,len(e)):
     if e[i][1]==e[i-1][1]:
          print(e[i][0],e[i][1])
