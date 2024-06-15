ls=eval(input())
a=sum(ls)/len(ls)
b=list(str(a))
if b[-1]=='0':
    print('%d'%(a))
else:
    print('%.2f'%(a))






