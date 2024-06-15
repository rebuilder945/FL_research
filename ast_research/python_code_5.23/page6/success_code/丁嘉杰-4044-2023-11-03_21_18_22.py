n=int(input())
def f(num):
    a=num
    temp=0
    while num!=0:
        temp+=(num%10)**3
        num=num//10
    if a==temp:
        print(a)
        return True
flag=0
for i in range(2,n+1):
    if f(i):
        flag=1
if flag==0:
    print("none")
