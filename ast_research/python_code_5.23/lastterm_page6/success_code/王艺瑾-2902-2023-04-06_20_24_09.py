a=1
b=2
n=eval(input())
c=0
sum=0
while c<n:
    sum=b/a+sum
    b=b+a
    a=b-a
    c+=1
print("%.4f"%(sum))

