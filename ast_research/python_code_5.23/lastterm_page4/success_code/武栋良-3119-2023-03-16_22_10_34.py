ls = eval(input())
for i in range(len(ls)):
    x = ls[i]
    i = i-1
    while ls.count(x)>1:
        ls.remove(x)
print(ls)
