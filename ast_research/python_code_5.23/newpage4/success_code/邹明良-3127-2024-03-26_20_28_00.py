a = int(input())
ls = [x+1 for x in range(a)]
ls.remove(1)
ls.append(1)
print(ls)

