a=input()
b={}
while a!="q":
    b[a]=b.get(a,0)+1
    a=input()
c=map(list(int,b.values()))
for i in range(len(b)):
    if int(c[i])==max(c):
        print(i,b[i])



