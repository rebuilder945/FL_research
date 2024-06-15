n,m,l = eval(input())
nums = [n]
for i in range(m-1):
    a = nums[-1]+l
    nums.append(a)
print(nums)

