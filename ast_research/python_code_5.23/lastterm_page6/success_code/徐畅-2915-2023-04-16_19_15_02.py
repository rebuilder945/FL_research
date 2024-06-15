i= eval(input())
e=0
for n in range(100,i+1):
    a=n//100
    b=(n-a*100)//10
    c=(n-a*100-b*10)
    if  a**3+b**3+c**3==n and n<=999:
        print(n)
        e=e+1
if e==0:
    print("none")



