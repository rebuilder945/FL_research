def search(list):
    n = len(list)
    for i in list:
        if list.count(i) > n/2:
            return i






nums = eval(input())
y = search(nums)
print(y)


