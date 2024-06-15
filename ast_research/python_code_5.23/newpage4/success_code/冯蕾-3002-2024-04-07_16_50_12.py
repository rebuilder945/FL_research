lst=eval(input())
eva=sum(lst)/len(lst)
if eva==int(eva):
    print(int(eva))
else:
    print('%.2f'%(eva))
