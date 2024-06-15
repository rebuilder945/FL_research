ls = eval(input())
lscopy = ls.copy()
count = 0
for i in range(len(lscopy)):
    count = ls.count(lscopy[i])
    if count!=1:
        for j in range(count-1):
            ls.remove(lscopy[i])
print(ls)

