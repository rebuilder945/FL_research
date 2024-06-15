s=eval(input())
ls=[]
if s=='':
    print('None')
else:
    for i in s:
        if not i in ls:
            ls.append(i)
    print(ls[0])


