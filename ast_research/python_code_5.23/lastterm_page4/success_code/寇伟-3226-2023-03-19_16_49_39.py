def search(lst):
    lst1=[]
    for i in range(len(lst)):
        a=lst.count(i)
        if a > len(lst)//2:
            lst1.append(i)
    if max(lst)>=1:
        return max(slt)
    else:
        return False





nums = eval(input())
y = search(nums)
print(y)


