a = list(eval(input()))
n,m = eval(input())
if (n>=0) and (n <= (len(a)-1)):
    b = [a[n]]*m
    a.extend(b)
    print(a)
else:
    print("error")
