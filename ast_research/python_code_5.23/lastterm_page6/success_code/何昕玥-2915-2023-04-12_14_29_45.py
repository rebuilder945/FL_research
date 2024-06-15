x=eval(input())
j=0
if 100<x<=999:
    for i in range(100,x+1):
        a=i%10
        b=i//10%10
        c=i//100
        if i==a**3+b**3+c**3:
            print(i)
            j+=1
elif x>999:
    for i in range(100,1000):
        a=i%10
        b=i//10%10
        c=i//100
        if i==a**3+b**3+c**3:
            print(i)
            j+=1
elif x<=100 or j==0:
    print("none")
        
