lst=eval(input())
average=sum(lst)/len(lst)
i=int(average)
if i<average:
    print('%.2f'%(average))
else:
    print(i)
