n=eval(input())
def shui(x):
    a=x%100
    b=(x//10)%10
    c=x//100
    a**3+b**3+c**3==x
for i in range(0,n+1):
    if shui(i):
        print(i)
    else:
        print("none")
        break
    
