a = list(eval(input()))
n,m = eval(input())
n1,m1 = int(n),int(m)
if n<len(a) :
    b = a[n]
    for i in range(m) :
        a.append(b)
    print(a)
else :
    print("error")
