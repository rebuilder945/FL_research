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
nums=eval(input())
find_unique1=','.join(str(i) for i in find_unique(nums))
print(find_unique1)
