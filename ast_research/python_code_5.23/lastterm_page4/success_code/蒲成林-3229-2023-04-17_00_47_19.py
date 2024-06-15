def find(nums):
    findnum=[]
    for i in nums:
        if nums.count(i)==1:
            findnum.append(i)
    if len(findnum)==0:
        return False
    else:
        return sorted(findnum)

nu=eval(input())
print(''.join(map(str,find(nu))))
