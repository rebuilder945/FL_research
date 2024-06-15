n=input().split()
dora={}
for i in n:
    dora[i]=dora.get(i,0)+1
max_=max(list(dora.values()))
ls=[]
for i,j in dora.items():
    if j==max_:
        ls.append(i)
ls.sort()
for i in ls:
    print(i,max_)

