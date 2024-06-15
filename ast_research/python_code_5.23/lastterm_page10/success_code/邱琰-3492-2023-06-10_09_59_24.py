n=list(input().split())
ls=[]
if len(n)==0:
    print('None')
else:
    for i in range(len(n)):
        if n[i] not in n[i+1:]:
            ls.append(n[i])
    print(ls[0])
