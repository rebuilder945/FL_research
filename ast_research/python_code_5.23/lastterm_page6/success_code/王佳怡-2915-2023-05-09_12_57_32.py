n=eval(input())
l=[]
def shui(x):
    a=x%100
    b=(x//10)%10
    c=x//100
    a**3+b**3+c**3==x
for i in range(0,n+1):
    if shui(i):
        l.append(i)
        print(i)
if len(l)==0:
    print("none")
    
