names = input().split(',')
mark = eval(input())
namelist = list(names)
ls = []
for i in range(len(mark)):
    ls.append([namelist[i],mark[i]])
print(ls)
