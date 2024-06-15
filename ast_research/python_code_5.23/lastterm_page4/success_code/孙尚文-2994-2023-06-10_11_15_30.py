a=input().split()

c,d=eval(input())
print(c)
if -len(a)<=int(c)<len(a):
    e=a[c]
    for i in range(int(d)):
        a.append(e)
    print(a)

else:
    print("error")
