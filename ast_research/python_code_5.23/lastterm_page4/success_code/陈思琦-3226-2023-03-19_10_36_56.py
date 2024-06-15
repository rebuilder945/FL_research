def search(nums):
    #search= max(set(nums), key=nums.count)
    d=int(nums.count(search))
    b=int(len(nums))
    c=b//2
    if d >=c:
        search= max(set(nums), key=nums.count)
        return search
    else:
        nums.clear()
        nums.append("False")
        return nums






nums = eval(input())
y = search(nums)
print(y)


