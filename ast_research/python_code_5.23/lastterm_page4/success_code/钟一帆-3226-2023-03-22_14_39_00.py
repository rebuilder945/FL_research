def search(n):
    for i in n:
        a=n.count(i)
        if a>(len(n)/2):
            return i 
        return False





nums = eval(input())
y = search(nums)
print(y)


