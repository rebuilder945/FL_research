a=[]
while True:
    s=input()
    if s!='q':
        a.append(s)
    else:
        break
b={}
for x in a:
    b[x]=a.count(x)
ls=[]
lt=[]
for k,v in b.items():
    ls.append([k,v])
    lt.append(int(v))
for x in ls:
    if x[1]==max(lt):
        print(x[0],x[1])
