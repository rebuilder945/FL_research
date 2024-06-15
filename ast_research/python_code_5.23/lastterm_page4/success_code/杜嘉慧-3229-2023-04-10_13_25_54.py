lst = eval(input())
new = []
flag = False
for x in lst:
    if lst.count(x) == 1:
        new.append(x)
        flag = True
new.sort()
if flag:
    print(*new, sep=',')
else:
    print(flag)



