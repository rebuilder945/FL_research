def search(nums):
    for x in nums:
        b=nums.count(x)
        n=[]
        n.append(b)
    if max(n)>len(nums)/2:
        print(x)
    else:
        print("False")
        





nums = eval(input())
y = search(nums)
print(y)


