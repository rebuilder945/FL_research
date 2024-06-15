total=eval(input())
k=0
if total<100:
    print("none")
elif 100<=total<=999:
    for i in range(100,total+1):
        a=i//100
        b=(i-100*a)//10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)
            k=1
    if k==0:
        print("none")
else:
    for i in range(100,999):
        a=i//100
        b=(i-100*a)//10
        c=i%10
        if a**3+b**3+c**3==i:
            print(i)
