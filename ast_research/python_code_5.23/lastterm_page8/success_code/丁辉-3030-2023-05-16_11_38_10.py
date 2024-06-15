names=input().split()
scores=input().split()
a=[[x,y] for x in names for y in scores]
a.sort(key=lambda x:x[1],reverse=True)
print(a)
