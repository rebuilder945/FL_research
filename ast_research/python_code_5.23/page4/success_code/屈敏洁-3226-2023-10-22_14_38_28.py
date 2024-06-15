def search(ls):
    for i in ls:
        if(ls.count(i)>len(ls)):
            return i
    return False       


    






nums = eval(input())
y = search(nums)
print(y)


