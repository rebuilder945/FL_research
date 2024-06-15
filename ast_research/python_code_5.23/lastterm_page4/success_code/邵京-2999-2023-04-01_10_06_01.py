pristr=input().split()
n,m=input().split()
n=int(n)
m=int(m)
liststr=list(pristr)
liststr[n],liststr[m]=liststr[m],liststr[n]
print(liststr)

