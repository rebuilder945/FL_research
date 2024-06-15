a=input().split()

c,d=eval(input())
if -len(a)<=c<len(a):
    e=a[c]
    for i in range(d):
        a.append(e)
    print(a)

else:
    print("error")
