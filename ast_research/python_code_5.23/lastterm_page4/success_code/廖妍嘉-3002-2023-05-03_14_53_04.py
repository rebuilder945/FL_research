ls=eval(input())
a=sum(ls)/len(ls)
if a-int(a)!=0:
    print('%.2f'%(a))
else:
    print(int(a))
