dyh=eval(input())
a,b=input().split(',')
a=int(a)
b=int(b)
if a<len(dyh) and b<len(dyh):
    if a<b:
        del dyh[a:b]
        print(dyh)
    else:
        del dyh[b:a:-1]
        print(dyh)
else:
    print("error")
