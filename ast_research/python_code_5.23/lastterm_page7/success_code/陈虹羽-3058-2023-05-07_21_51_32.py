a={}
c=[]
x=input()
while  (x!='q'):
    a[x]=a.get(x,0)+1
    x=input()
for k,v in a.items():
    c.append([k,v])       
c.sort(key=lambda x:x[1],reverse=True)
m,n=c[0]
print(m,n)

