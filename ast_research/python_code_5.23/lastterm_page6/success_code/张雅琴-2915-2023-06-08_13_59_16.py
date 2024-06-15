def flow(a):
    number=a
    s=0
    while a>0:
        s+=(a%10)**3
        a//=10
    if s==number:
        print(s)
        return True
a=eval(input())
b=0
for i in range(2,a+1):
    if flow(i):
        b=1
if b==0:
    print("none")

