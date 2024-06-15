def search():
    a=input()
    n=len(a)
    for i in range(a):
        if a.count(i)>(n//2):
            print(i)
        else:
            print('False')





nums = eval(input())
y = search(nums)
print(y)


