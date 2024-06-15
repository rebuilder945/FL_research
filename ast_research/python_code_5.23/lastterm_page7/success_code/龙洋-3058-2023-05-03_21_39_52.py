x  =  input()
dian={}
while x != 'q':
    dian[x]=dian.get(x,0)+1
    x=input()
lis=list(dian.items())
lis.sort(key=lambda x: x[1],reverse=True)
print(lis[0][0],lis[0][1])

