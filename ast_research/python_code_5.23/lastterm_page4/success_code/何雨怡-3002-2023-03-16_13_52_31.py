lst=eval(input())
sum=sum(lst)
num=len(lst)
average=sum/num
if average%1==0:
    print(int(average))
else:
    print('%.2f'%(average))
