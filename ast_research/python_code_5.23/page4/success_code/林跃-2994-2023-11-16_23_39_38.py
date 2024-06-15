a=eval(input())
c=a.count(0)
n,m=eval(input())
if n>=len(a):
    print("error")
b=c[n]*3
a.append(b)
print(a)
