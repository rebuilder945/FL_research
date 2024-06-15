x=eval(input())
j=0
if x<=100:
    print("none")
elif x>100:
    for i in range(100,x):
        a=i%10
        b=i//10%10
        c=i//100
        if i==a**3+b**3+c**3:
            print(i)
            j+=1
if j==0:
    print("none")
        
