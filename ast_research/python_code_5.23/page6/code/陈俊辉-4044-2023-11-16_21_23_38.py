def flower(number):
    a=number
    n=0
while number!=0:
    n+=(number%10)**3
    number=number//10
    if a==n:
        print(a)
        return True
m=o
number=eval(input())
for i in range(2,number+1):
    if flower(i):
        m=1
    if m==0:
        print("none")

    




