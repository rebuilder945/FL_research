lst=eval(input())
a=sum(lst)/len(lst)
if a==int(a):
    print(a)
else:
    print('%.2f'%(a))
