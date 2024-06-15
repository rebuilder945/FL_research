n=eval(input())
a=False
for i in range(100,n+1):
    a=int(str(i)[0])
    b=int(str(i)[1])
    c=int(str(i)[2])
    if a**3+b**3+c**3==i:
        print(i)
        a=True
if not a:
    print("none")

