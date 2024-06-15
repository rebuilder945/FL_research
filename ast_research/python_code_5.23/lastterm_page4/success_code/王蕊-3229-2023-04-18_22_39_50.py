def search(y):
    for x in y:
        if (y.count(x) ==1):
            return x
        return False
nums  =  eval(input())
y  =  search(nums)
print(y)

