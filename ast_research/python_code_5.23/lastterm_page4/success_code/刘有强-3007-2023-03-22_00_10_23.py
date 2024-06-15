dyh=eval(input())
a,b=input().split(',')
a=int(a)
b=int(b)
if a<b<len(dyh):
    del dyh[a:b]
    print(dyh)
elif b<a<len(dyh):
    del dyh[b:a:-1]
    print(dyh)
else:
    print("error")
