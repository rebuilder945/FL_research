nums = eval(input())
n,m = eval(input())
for i in range(n,m):
    if n<=m:
        nums.pop(i)
    print(nums)
else:
    print("error")
