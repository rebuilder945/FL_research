list=list(map(int,input().strip('[]').split(',')))
sum=sum(list)
sum=sum/len(list)
if sum%1==0:
    sum=int(sum)
    print(sum)
else:
    print('%.2f'%sum)
