a=eval(input())
for x in range(100,a+1):
    A=x//100%10
    B=x//10%10 
    C=x%10
    if x==A**3+B**3+C**3:
        print(x)
else:
        print("none")


