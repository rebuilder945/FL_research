def search(nums):
    ls=[]
    for i in nums:
        if i not in ls:
            ls.append(i)
    for x in ls:
        if x>len(nums)//2:
            return(x)
        else:
            return('False')





nums = eval(input())
y = search(nums)
print(y)


