def search(num):
    for i in num:
        n=num.count(i)
        if n>len(num)//2:
            return i
        return False





nums = eval(input())
y = search(nums)
print(y)


