def search(mnums):
    cishu=[]
    for i in nums:
        a=nums.count(i)
        cishu.append(a)
    if max(cishu)>1:
        mnums=max(set(nums),key=nums.count)
    else:
        mnums="False"
    return mnums





nums = eval(input())
y = search(nums)
print(y)


