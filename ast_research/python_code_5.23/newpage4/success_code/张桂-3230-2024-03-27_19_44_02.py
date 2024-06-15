ls = eval(input())
ls.sort(key=int,reverse=True)
ls1 = "".join(map(str,ls))
print(ls1)
