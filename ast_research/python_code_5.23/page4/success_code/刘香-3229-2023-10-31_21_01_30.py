ls=eval(input())
lsone=[]
for i in ls :
    if ls.count(i)==1:
        lsone.append(i)
        lsone.sort()
        print(lsone)
    else:
        print('False')
