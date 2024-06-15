lsname=list(input().split(','))
lsscore=eval(input())

ls=[[x,y] for x,y in zip(lsname,lsscore)]

print(ls)
