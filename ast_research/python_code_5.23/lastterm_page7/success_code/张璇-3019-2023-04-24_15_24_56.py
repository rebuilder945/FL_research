a,b,c,d=input().split()
e={}
e['english']=int(b)
e['python']=int(c)
e['math']=int(d)
f=list(e.items())
f.sort(key=lambda x:x[1],reverse=True)
g=(int(b)+int(c)+int(d))/3
f.append(g)
print("%s %.2f %.2f %.2f %.2f"%(a,f[0][1],f[1][1],f[2][1],f[3]))
