def search(nums):
    n=len(search)
    for x in nums:
        if search.count(x) > n//2:
            print(x)
        else:
            print("False")





nums = eval(input())
y = search(nums)
print(y)


