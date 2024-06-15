def search(lst):
    length=len(lst)
    for i in lst:
        if lst.count(i)>=length*0.5:
            return i
        else:
            return 'False'





nums = eval(input())
y = search(nums)
print(y)


