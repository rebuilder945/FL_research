def find_unique(nums):
    count={}
    for num in nums:
        if num not in count:
            count[num]=1
        else:
            count[num]+=1
    unique=[]
    for num in count:
        if count[num]==1:
            unique.append(num)
    if not unique:
        return False
    else:
        return sorted(unique)
unique=','.join(str(i) for i in find_unique(nums))
nums=eval(input())
print(find_unique(nums))
