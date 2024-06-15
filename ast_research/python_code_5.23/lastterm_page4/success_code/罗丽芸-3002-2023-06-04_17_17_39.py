ls=eval(input())
aver=sum(ls)/len(ls)
if aver%1==0:
    print(int(aver))
else:
    print('%.2f'%aver)
