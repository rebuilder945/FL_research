nums=eval(input())
def find_unique(nums):
    count={}
    for num in nums:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    unique_nums=[]
    for num in count:
        if count[num]==1:
            unique_nums.append(num)
    if len(unique_nums)==0:
        return "False"
    else:
        return sorted(unique_nums)
find_unique1=[]
for i in find_unique:
    find_unique1.append(str(i))
print(find_unique1)
