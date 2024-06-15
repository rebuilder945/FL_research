a=list(input())
b,c=map(int,input().split(","))
if b>=len(a) or c>=len(a) or b>=c:
    print("error")
else:
    s=a.pop(b,c)
    print(s)

