pristr=input()
n,m=eval(input().split())
liststr=list(pristr)
liststr[n],[m]=liststr[m],[n]
print(liststr)

