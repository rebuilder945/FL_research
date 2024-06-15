nums = eval(input())
n,m = eval(input())
if n<=m:
    for i in range(n,m):
        nums.pop(i)
    print(nums)
else:
    print("error")
