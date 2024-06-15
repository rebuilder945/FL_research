ls={}
ls1=[]
s=input()
while s!="q":
    ls[s]=ls.get(s,0)+1
    s=input()
for s,v in ls.items():
    ls1.append([s,v])
    ls1.sort(key=lambda x:x[1],reverse=True)
print("".join(ls1[0]))



