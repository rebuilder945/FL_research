def search(a):
    for x in a:
        b=a.count(x)
        if b>(len(a))/2:
            return x
            break
        else:
            continue
    return "False"






nums = eval(input())
y = search(nums)
print(y)


