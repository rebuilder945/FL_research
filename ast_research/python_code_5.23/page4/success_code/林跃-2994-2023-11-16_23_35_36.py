a=eval(input())
n,m=eval(input())
b=a.count()
if n>=len(a):
    print("error")
b=a[n]*3
a.append(b)
print(a)

