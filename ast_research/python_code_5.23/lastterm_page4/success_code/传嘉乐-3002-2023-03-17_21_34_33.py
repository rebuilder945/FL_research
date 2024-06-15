ls=eval(input())
a=sum(ls)/len(ls)
if type(a)=='int':
    print('%d'%a)
else:
    print('%2f.d'%(a))

