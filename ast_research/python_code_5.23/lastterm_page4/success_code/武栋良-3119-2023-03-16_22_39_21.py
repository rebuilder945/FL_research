ls = eval(input())
i = 0
while i<len(ls):
    if ls.count(ls[i])>1:
        ls.remove(ls[i])
    else:
        i = i+1
print(ls)

