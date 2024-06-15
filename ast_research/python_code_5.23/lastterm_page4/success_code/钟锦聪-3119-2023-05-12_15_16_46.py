sum = eval(input())
nums =[]
for x in sum:
    if x not in nums:
        nums.append(x)
for x in nums:
    a = sum.count(x)
    if a > 1:
        for i in range(a-1):
            sum.remove(x)
print(sum)

