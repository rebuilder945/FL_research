a=[]
def search(nums):
    for x in nums:
        n=nums.count(x)
        if not n in a:
            a.append(n)
    m=max(a)
    if m>len(nums)/2:
        return m
    else:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


