nums = eval(input())
def search(nums):
    for x in nums:
        if count(x)>=len(nums)/2:
            y = search(nums)
            print(y)
        else:
            print("False") 





nums = eval(input())
y = search(nums)
print(y)


