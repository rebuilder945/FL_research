a = float(input())
b = int(input())
nums=[a]
i=1
while i < b:
    i = i+1
    nums.append(a)
    a= a/2
s=sum(nums)
print("%.2f" %(s))

