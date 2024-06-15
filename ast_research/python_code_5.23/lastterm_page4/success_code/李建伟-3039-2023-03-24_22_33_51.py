def delete(nums):
    mx = max(nums)
    mn = min(nums)
    #法二
    lst2 = []
    for i in nums:
        if mn < i < mx:
            lst2.append(i)
    return lst2
            
    #法一
    # while mx in nums:
    #     nums.remove(mx)
    # while mn in nums:
    #     nums.remove(mn)
    # return nums
lst = eval(input())
lst1 = delete(lst)
print(lst1)

