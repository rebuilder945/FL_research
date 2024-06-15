def flower(number):
    a=number
    temp=0
    while number!=0:
        temp+=(number%10)**3
        number=number//10
    if a==temp:
        print(a)
        return True


flag=0
number=int(input())
for i in range(2,number+1):
    if flower(i):
        flag=1
if flag==0:
    print('none')


