n = int(input())
ls =[i for i in range(1,n+1)]
a = ls[0]
ls.pop(0)
ls.append(a)
print(ls)
