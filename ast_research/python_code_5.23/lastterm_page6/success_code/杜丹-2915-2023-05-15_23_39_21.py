a=int(input())
c=0
for b in range(99,a+1):
    if (b//100)**3+(b//10%10)**3+(b%10)**3==b and b<1000:
        print(b)
        c=c+1
if c==0:
    print("none")

