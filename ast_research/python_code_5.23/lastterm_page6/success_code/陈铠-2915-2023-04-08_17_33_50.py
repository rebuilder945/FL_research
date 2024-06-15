n=eval(input())
a=False
for i in range(1,n+1):
    a=int(str(n)[0])
    b=int(str(n)[1])
    c=int(str(n)[2])
    if a**3+b**3+c**3==n:
        print(n)
        a=True
if not a:
    print("none")

