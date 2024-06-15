dian={}
lis1=[]
lis=input().split()
for x in lis:
    dian[x]=dian.get(x,0)+1
for k,v in dian.items():
    lis1.append([k,v])
lis1.sort( key=lambda x:x[1],reverse=True)
n=len(lis1)
a=1
for w in range(n-1):
    if lis1[0][1]==lis1[w+1][1]:
        a=a+1 
for u in range(a):
    print(lis1[u][0],lis1[u][1])
    

