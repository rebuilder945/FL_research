a=list(eval(input()))
n,m=eval(input())
s=[]
s.extend(a[0:n])
s.extend(a[m:-1])
print(s)
