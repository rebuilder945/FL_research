pristr=input()
n,m=input().split()
liststr=list(pristr)
liststr[n],[m]=liststr[m],[n]
print(liststr)

