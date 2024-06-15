lst=eval(input())
avg=sum(lst)/len(lst)
if avg%1==0:
    print(int(avg))
else:
    print('%.2f'%avg)
