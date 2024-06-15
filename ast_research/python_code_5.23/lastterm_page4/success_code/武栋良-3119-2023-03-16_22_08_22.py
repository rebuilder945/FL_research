ls = eval(input())
for i in range(len(ls)):
    x = ls[i]
    while ls.count(x)>1:
        ls.remove(x)
        i = i-1
print(ls)
