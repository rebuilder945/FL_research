def shui(x):
    a=x
    temp=0
    while x!=0:
        temp+=(x%10)**3
        x=x//10
    if a==temp:
        print(a)
        return True
flag=0   
x=eval(input())
for i in range(0,x+1):
    if shui(i):
        flag=1
if flag==0:
    print("none")
