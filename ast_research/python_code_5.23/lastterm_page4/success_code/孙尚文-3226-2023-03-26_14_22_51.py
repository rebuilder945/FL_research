def search(nums,n):
    for x in range(n):
        if nums.count(x)>(n/2):
            print(x)
        if nums.count(x)<=(n/2):
            print("false")





nums = eval(input())
y = search(nums)
print(y)


