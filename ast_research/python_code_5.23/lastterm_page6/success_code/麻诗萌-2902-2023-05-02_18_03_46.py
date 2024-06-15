n=eval(input())
lst=[2/1]
m=2
q=1
for i in range(n-1):
    m0=m
    q0=q
    m=m0+q0
    q=m0
    s=m/q
    lst.append(s)
print("%.4f"%sum(lst))
