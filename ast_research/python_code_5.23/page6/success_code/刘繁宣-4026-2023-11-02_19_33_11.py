n=eval(input())
s=0
def F(nums):
    if nums<2:
        return nums
    else:
        a,b = 0,1
        for i in range(nums):
            a,b = b,a+b
        return b 
for i in range(n):
    s += F(i+2)/F(i+1)
print("%.4f"%s)
