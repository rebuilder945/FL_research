a = list(eval(input()))
n,m = eval(input())
if n>len(a)-1:
    print("error")
else:
    b = [a[n]]*m
    print(a+b)
