num=int(input())
m=0
for n in range(100,num+1):
    if n<1000:
        c=int(n%10)
        b=int(n//10%10)
        a=int(n//10//10)
        if a**3+b**3+c**3==100*a+10*b+c:
            print(100*a+10*b+c)
            m=1
if m ==0:
    print("none")




