lst=(input().split())
lstnum=(input().split())
a=eval(lstnum[0])
b=eval(lstnum[1])

c=lst[b]
lst[b]=lst[a]
lst[a]=lst[b]

