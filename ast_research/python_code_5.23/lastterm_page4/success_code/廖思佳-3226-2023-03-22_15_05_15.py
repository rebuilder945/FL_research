def search(n):
    for x in n:
        if x.count(n)>n//2:
            return x
        else:
            print("False")
    





nums = eval(input())
y = search(nums)
print(y)


