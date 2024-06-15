lst = []
def search(nums):
    t = int(len(nums)//2)
    for x in nums:
        if x not in lst:
            if nums.count(x)>t:
                lst.append(x)
            else:
                pass
        else:
            pass        
    if bool(lst) == False: 
        return False        
    else :
        return lst[0]   





nums = eval(input())
y = search(nums)
print(y)


