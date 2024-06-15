def search(n):
    dict={}
    for i in n:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    x=max(dict.values())
    a=n.count(x)
    if a> len(n)/2:
        return x
    else:
        a<= len(n)/2
        return False





nums = eval(input())
y = search(nums)
print(y)


