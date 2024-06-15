def search(x):
    jishu=0
    for x1 in x:
        if x.count(x1)>len(x)/2:
            print(x1)  
        else:
            print(False)





nums = eval(input())
y = search(nums)
print(y)


