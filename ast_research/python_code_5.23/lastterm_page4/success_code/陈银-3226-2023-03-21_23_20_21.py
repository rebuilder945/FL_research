def search(a):
    n = len(a)
    for x in a:
        if a.count(x)>n//2:
            return a.count(x)
        else:
            return "False"
    
   





nums = eval(input())
y = search(nums)
print(y)


