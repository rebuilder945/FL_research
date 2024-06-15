a = list(eval(input()))
n,m = eval(input())
b = a[0:n]
c = a[m:-1]
d = b+c
if n,m<=len(a) or n,m>=len(a):
    print("error")
else:
    print(d)

