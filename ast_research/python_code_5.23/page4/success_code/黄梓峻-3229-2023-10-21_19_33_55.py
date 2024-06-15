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
        print("False")
    else:
        return sorted(unique_nums)
print (str(find_unique(nums)))
