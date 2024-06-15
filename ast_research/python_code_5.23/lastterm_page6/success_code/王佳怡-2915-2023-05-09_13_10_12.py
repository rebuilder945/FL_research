def shui(x):
    a=x%100
    b=(x//10)%10
    c=x//100
    a**3+b**3+c**3==x
l=[]    
n=eval(input())
for i in range(0,n+1):
    if shui(i):
        print(i)
        l.append(i)
if len(l)==0:
    print("none")
