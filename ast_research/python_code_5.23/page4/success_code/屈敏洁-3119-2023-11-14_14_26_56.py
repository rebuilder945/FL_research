ls = eval(input())
for i in ls.copy():
    if ls.count(i)>1:
        ls.remove(i)
print(ls)       
