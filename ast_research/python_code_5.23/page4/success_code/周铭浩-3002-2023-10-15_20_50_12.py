ls=eval(input())
ave=sum(ls)/len(ls)
if ave%1==0:
    a=int(ave)
    print(a)
else:
    print('%.2f'(ave))

