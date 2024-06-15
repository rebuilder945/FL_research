a = eval(input())
b,c = eval(input())
if  c<len(a) and b<c:
    m = a[0:b]
    n=a[c: ]
    h = m+n
    print(h)
else :
    print("error")







