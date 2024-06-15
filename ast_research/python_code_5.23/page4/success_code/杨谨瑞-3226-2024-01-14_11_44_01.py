def search(nums):
    num=len(nums)//2
    setnum=list(set(nums))
    for i in range(len(setnum)):
        counter=0
        for j in range(len(nums)):
            if setnum[i]==nums[j]:
                counter+=1
            if counter>num:
                return setnum[i]
    return 'False'






nums = eval(input())
y = search(nums)
print(y)


