n=int(input())
i=1
a=2
b=1
nums=[]
while i<=n:
    nums.append(a/b)
    a=a+b
    b=b+1
    i=i+1
x=sum(nums)
print("%.4f"%(x))
