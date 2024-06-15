def search(nums):
    search= max(set(nums), key=nums.count)
    d=int(nums.count(search))
    b=int(len(nums))
    c=b//2
    if d >=c:
        return search
    else:
        search.clear()
        search.append("False")
        return search






nums = eval(input())
y = search(nums)
print(y)


