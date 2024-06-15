def search(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    l = list(dic)
    for i in l:
        if l[i][1]>=l[i][0]//2:
            return i[0]
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


