ls=eval(input())
a=sum(ls)/len(ls)
if type(a)=='int':
    print(int(a))
else:
    print('%2f.d'%(a))

