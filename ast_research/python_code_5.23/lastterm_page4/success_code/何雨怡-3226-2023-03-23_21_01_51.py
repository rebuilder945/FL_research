def search(lst):
    length=len(lst)
    for i in lst:
        if lst.count(i)>length//2:
            return i
        else:
            return 'False'





nums = eval(input())
y = search(nums)
print(y)


