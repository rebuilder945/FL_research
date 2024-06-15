n,m,l = eval(input())
nums = []
for x in range(m):
    if len(nums) == 0:
        nums.append(n)
    else:
        n += l
        nums.append(n)
print(nums)



