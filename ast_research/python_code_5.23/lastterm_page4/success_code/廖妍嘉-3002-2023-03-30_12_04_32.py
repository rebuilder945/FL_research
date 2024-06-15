ls=eval(input())
a=sum(ls)/len(ls)
if a-eval('%d'%(a))>0:
    print('%.2f'%(a))
else:
    print('%d'%(a))
