n = eval(input())
ls = [x for x in range(1,n+1)]
ls2 = ls[1:]
ls2.append(ls[0])
print(ls2)
