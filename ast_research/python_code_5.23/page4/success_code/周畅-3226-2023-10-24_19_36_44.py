def search(n):
    for x in n:
        a=n.count(x)
        if a> len(n)/2:
            print(x)
        else:
            a<= len(n)/2
            print(False)





nums = eval(input())
y = search(nums)
print(y)


