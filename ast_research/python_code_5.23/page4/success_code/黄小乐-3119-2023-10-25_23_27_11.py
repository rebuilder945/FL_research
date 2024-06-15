ls = list(eval(input()))
ls2 = []
ls.reverse()
for i in ls:
    if i not in ls2:
        ls2.insert(0,i)
print(ls2)






