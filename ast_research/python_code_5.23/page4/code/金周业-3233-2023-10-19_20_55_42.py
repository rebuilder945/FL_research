n, m = eval(input())
nums = [x if nums%2 == 0 for x in range(n,m,2) else for x in range(n-1,m,2)]



print(nums)


