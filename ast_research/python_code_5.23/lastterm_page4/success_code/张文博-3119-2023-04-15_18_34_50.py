m=eval(input())
a,b=eval(input())
if b>=a and b<len(m):
    n=m[0:a]+m[b::]
    print(n)
else:
    print("error")

