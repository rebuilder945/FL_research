nums=eval(input())
n1=nums.copy()
for i in nums:
    if i==0:
        n1.remove(0)
        n1.append(0)
    else:
        pass
print(n1)

