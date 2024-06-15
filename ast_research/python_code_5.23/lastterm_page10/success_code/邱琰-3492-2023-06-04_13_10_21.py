a=input()
n=[i for i in a]
ls=[]
for i in range(len(n)):
    if n[i] not in n[i+1:]:
        ls.append(n[i])
if len(ls)!=0:
    print(ls[0])
else:
    print('None')
