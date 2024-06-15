num=eval(input())
x=0
while num>0:
    x*=10
    x+=(num%10+5)%10
    num//=10
print(x)
