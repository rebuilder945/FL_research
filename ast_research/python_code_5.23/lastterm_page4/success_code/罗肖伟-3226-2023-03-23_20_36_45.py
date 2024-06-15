def search(lst):
    lst1=[]
    for i in range (len(lst)):
        a=lst.count(i)
        if a>len(lst)//2:
            lst1.qppend(i)
        if lst1:
            return max(lst1)
        else:
            return  False





nums = eval(input())
y = search(nums)
print(y)


