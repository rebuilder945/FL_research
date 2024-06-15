n=eval(input())
ls=[x+1 for x in range(n)]
ls.append(ls.pop(0))
print(ls)
