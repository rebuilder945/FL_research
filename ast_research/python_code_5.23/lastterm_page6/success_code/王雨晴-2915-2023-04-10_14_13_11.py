def huahua(x):
    a=x
    b=0
    while x!=0:
        b=b+(x%10)**3
        x=x//10
    if a==b:
        print(a)
        return True
c=0
x=int(input())
for i in range(2,x+1):
    if huahua(i):
        c=1
if c==0:
    print("none")
