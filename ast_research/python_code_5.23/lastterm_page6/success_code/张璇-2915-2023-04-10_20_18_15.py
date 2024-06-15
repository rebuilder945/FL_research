a=eval(input())
i=0
if a>=100:
    for x in range(100,a):
        C=x%10
        B=x//10%10
        A=x//100
        if A**3+B**3+C**3==x:
            i+=1
            print(x)
    if i!=0:
        print("none")
else:
    print("none")
 
