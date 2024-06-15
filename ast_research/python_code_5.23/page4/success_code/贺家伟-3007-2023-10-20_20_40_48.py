a=list(input())
b,c=map(int,input().split(","))
if b>=c:
    print("error")
else:
    s=a.pop[b:c]
    print(s)

