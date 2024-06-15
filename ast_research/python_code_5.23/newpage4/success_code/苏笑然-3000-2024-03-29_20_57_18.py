list=list(map(int,input().strip('[]').split(',')))
sum=sum(list)
sum=sum/len(list)
print('%.2f'%sum)
