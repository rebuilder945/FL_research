a = int(input())
nums=[]
x=2
y=1
i=1
while i <= a:
    nums.append(float(x/y))
    x = y + x  
    y = x - y
    i = i + 1
s=float(sum(nums))
print("%.4f" % (s))
    
    


