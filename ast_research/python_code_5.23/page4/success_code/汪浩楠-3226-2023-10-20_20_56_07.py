def search(a):
    for i in a:
        b=a.count(i)
        if b>(len(a)/2):
            return i   
        else:
            print("False")
            break





nums = eval(input())
y = search(nums)
print(y)


