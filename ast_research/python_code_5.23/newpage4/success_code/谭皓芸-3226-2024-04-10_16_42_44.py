def search(nums) :
    x = []
    for i in nums :
        x.append(nums.count(i))
    if max(x) > len(nums)//2 :
        for i in nums :
            if nums.count(i) == max(x) :
                break
        return i
    else :
        return "False"





nums = eval(input())
y = search(nums)
print(y)


