a=eval(input())
sum=0
for i in range(len(a)):
    sum+=a[i]
b=sum/len(a)
if sum%len(a)==0:
    print(b)
else:
    print('%.2f'%b)
