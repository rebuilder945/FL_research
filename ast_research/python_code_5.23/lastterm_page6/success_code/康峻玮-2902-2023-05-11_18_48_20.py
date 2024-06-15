n=eval(input())
nums=[]
x=2
y=1
i=1
while i <= n:
    nums.append(x/y)
    x=x+y
    y=x-y
    i=i+1
s=sum(nums)
print("%.4f" % (s))
