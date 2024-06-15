n = int(input())
ls = [i for i in range(1,n+1)]
ls.insert(n,ls[0])
ls.remove(ls[0])
print(ls)
