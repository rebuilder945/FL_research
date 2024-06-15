m=input()
a,b=eval(input())
if a>-1 and b>a and b<len(m):
    m=m[0:a-1]+m[b:-1]
    print(m)
else:
    print("error")

