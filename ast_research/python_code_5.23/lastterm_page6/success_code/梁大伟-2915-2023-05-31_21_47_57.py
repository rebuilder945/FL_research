n=eval(input())
flag=1
for i in range(100,n+1):
    if i<=999 and (i%10)**3+(i//10%10)**3+(i//100)**3==i:
        print(i)
        flag=0
if flag==1:
    print('none')
