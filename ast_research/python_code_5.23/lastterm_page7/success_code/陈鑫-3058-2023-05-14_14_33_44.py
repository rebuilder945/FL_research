a=input()
b={}
while a!="q":
    b[a]=b.get(a,0)+1
    a=input()
for i in b:
    if int(b[i])==max(int(b.values())):
        print(i,b[i])



