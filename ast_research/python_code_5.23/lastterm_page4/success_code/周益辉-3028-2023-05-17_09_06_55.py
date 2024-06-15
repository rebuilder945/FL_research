# n,m,l=eval(input())
# x=n+l*m
# nums=list(range(n,x,l))
# print(nums)

n,m,l=eval(input())
a=[]
while m>0:
    a.append(n)
    n+=l
    m-=1
print(a)
