lst = eval(input())
sum = sum(lst)/len(lst)
sum1 = int(sum)
if not sum-sum1 == 0:
    print('%.2f'%(sum))
else:
    print(int(sum))
