ls=eval(input())
a=sum(ls)/len(ls)
print(a)
if len(str(a))==3:
    print('%d'%(a))
else:
    print('%.2f'%(a))






