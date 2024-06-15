def search(nums):
    search= max(set(nums), key=nums.count)
    d=nums.count(search)
    b=len(nums)
    c=b//2
    if d >=c:
        return search
    else:
        print("False")






nums = eval(input())
y = search(nums)
print(y)


