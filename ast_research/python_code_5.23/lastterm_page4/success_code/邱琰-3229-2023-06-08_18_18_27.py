n=eval(input())
ls=[]
for i in n:
    if i not in ls:
        ls.append(str(i))
if len(ls)!=0:
    ls.sort(reverse=True)
    print(''.join(ls))
else:
    print('False')
