nums = list(eval(input()))
lst = []
n = nums[0]
m = nums[1]
l = nums[2]
for i in range(n,n+m*l,l):
    lst.append(i)
print(lst)

