a=eval(input())
i=0
if 100<=a<1000:
    for x in range(100,a+1):
        C=x%10
        B=x//10%10
        A=x//100
        if A**3+B**3+C**3==x:
            i+=1
            print(x)
    if i==0:
        print("none")
elif a>=1000:
    for x in range(100,999):
        C=x%10
        B=x//10%10
        A=x//100
        if A**3+B**3+C**3==x:
            i+=1
            print(x)
    if i==0:
        print("none")
else:
    print("none")
 
