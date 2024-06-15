m=input()
a,b=eval(input())
if b>=a and b<len(m):
    m=m[0:a-1]+m[b:-1]
    print(list(m))
else:
    print("error")

