def search(list):
    b=max(set(list),key=list.count)
    if list.count(b)>len(list)//2:
        return(b)
    else:
        return("False")





nums = eval(input())
y = search(nums)
print(y)


