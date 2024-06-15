ls = eval(input())
for i in range(len(ls)):
    i = i-i
    x=ls[i]
    while ls.count(x)>1:
        ls.remove(x)
print(ls)
