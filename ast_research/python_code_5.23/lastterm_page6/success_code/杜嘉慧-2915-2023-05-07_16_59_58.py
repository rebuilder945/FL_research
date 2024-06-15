def flower(number):
    m=number
    temp=0
    while number!=0:
        temp+=(number%10)**3
        number=number//10
    if m==temp:
       print(m)
       return True
number=int(input())
flag=0
for x in range(2,number+1):
    if flower(x):
        flag=1
if flag==0:
    print("none")

