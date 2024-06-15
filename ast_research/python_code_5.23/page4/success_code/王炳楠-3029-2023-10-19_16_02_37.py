op=input()
nm=op.split(",")
cj=eval(input())
n=len(nm)
ed=[[] for _ in range(n)]
for i in range(n):
    ls0=[]
    a=cj[i]
    ls0.append(nm[i])
    ls0.append(a)
    ed[i]=ls0
print(ed)


