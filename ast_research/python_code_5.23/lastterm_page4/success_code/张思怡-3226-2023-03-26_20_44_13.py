def search(a): 
    n=len(a)
    for i in a:
        if a.count(i)>(n//2):
            return i
        else:
            return a.count(i)>(n//2)





nums = eval(input())
y = search(nums)
print(y)


