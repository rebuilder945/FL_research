a=eval(input())
ave=sum(a)/len(a)
if ave-ave//1==0:
    print('%d'%ave)
else:
    print('%.2f'%ave)
