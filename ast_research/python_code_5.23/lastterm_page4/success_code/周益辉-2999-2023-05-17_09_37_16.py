a=list(input().split())
b,c=map (int,input())
if b>len(a):
    print("error")
elif c>len(a):
    print("error")
else:
    eva=a[b]
    a[b]=a[c]
    a[c]=eva
print(a)
