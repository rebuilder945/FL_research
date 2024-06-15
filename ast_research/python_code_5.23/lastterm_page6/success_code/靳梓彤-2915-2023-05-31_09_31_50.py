n=eval(input())
count=0
for n in range(100,n+1):
    a=n%10
    b=n//10%10
    c=n//100%10
    if n==(a**3)+(b**3)+(c**3):
        print(n)
        count=count+1
if count==0:
    print("none")
