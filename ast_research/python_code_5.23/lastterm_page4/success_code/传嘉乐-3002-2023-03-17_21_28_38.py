ls=eval(input())
a=sum(ls)/len(ls)
if type(a)=='float':
    print('%2f.d'%(a))
else:
    print('%.d'%a)

