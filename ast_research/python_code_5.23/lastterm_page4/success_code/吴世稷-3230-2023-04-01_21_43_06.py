ls = eval(input())
ls.sort()
ls1 = []
ls1.append(ls[0])
for x in range(2,len(ls)+1):
    if ls[x-1]*(10**(x-1)) not in ls1:
        ls1.append((ls[x-1]*(10**(x-1))))
    else:
        ls1 = ls1[0:]
print(ls)
print(ls1)
print(sum(ls1))
