a = eval(input())
c,d = eval(input())
if c < len(a):
    if d < len(a):
        a[c:d]=[]
    else:
        a[c:]=[]
    print(a)
if c > len(a):
    print("error")


