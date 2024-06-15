def search(sb):
    lst=[sb.count(i) for i in sb]
    if max(lst)<=len(sb)//2:
        return"False"
    else:
        for x in sb:
            if sb.count(x)==max(lst):
                return(x)





nums = eval(input())
y = search(nums)
print(y)


