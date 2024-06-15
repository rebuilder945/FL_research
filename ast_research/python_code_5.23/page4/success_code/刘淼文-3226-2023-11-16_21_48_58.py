def search(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    l = list(dic)
    for i in l:
        if int(i[1])>=int(i[0]):
            return i[0]
        else:
            return False





nums = eval(input())
y = search(nums)
print(y)


