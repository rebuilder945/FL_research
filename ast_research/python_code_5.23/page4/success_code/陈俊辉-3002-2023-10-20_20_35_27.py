def list_sum(a):
    c=0
    for num in a:
        c+=num
    return c    
a=list(input())
b=len(a)
c=list_sum(a)
d=c/b
a=3.14
if d%1==0:
    print(d)
elif d%1!=0:
    print("%.2f"%(d))
