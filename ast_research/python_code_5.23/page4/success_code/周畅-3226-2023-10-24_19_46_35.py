def search(n):
    for x in n:
        from collections import Counter
        count=Counter(x)
        a=n.court()
        return a
        if a> len(n)/2:
            print(x)
        else:
            a<= len(n)/2
            print(False)





nums = eval(input())
y = search(nums)
print(y)


