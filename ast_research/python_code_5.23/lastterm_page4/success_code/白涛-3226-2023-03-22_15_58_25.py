def search(n):
    a=list(n)
    for i in a:
        if a.count(i) > len(a)/2:
            print(i)
        else:
            print("False")





nums = eval(input())
y = search(nums)
print(y)


