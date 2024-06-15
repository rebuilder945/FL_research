n=input()
ls=[]
if len(n)==0:
    print('None')
else:
    for i in range(len(n)):
        if n[i] not in n[i+1:]:
            ls.append(n[i])
    if len(ls)==0:
        print('None')
    else:
        print(ls[0])
