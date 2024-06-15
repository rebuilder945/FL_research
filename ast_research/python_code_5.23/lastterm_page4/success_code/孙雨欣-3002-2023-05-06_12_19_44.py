ls1=eval(input())
sum=0
for i in ls1:
    sum+=i
ave=sum/len(ls1)
if int(ave)==ave:
    print(int(ave))
else:
    print('%.2f'%ave)
