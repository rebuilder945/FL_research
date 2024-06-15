numbers=eval(input())
average=sum(numbers)/len(numbers)
averagestr=str(average)
d=averagestr.count('.')
if averagestr[d+1]==0 and averagestr[d+2]==0:
    print(int(averagestr))
else:
    print('%.2f'%average)

