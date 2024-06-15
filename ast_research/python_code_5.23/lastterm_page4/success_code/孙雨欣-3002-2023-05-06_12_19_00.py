ls1=eval(input())
sum=0
for i in ls1:
    sum+=i
ave=sum/len(ls1)
if int(sum)==sum:
    print(int(sum))
else:
    print('%.2f'%sum)
