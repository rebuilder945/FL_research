def search(y):
    n=len(y)
    for i in y:
        if y.count(i)>n//2:
           return i;
    return False;





nums = eval(input())
y = search(nums)
print(y)


