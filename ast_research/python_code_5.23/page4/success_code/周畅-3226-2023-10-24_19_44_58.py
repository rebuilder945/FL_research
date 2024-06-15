def search(n):
    for x in n:
        from collections import Counter
        count=Counter(n)
        a=count.n(1)[0][0]
        return a
        if a> len(n)/2:
            print(x)
        else:
            a<= len(n)/2
            print(False)





nums = eval(input())
y = search(nums)
print(y)


