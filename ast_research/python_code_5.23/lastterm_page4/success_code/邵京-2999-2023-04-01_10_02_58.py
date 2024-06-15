pristr=input()
n,m=input().split()
n=int(n)
m=int(m)
liststr=list(pristr)
liststr[n],[m]=liststr[m],[n]
print(liststr)

