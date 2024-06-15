ls = eval(input('请输入列表:'))
for x in ls:
    while ls.count(x)>1:
        ls.remove(x)
print(ls)
