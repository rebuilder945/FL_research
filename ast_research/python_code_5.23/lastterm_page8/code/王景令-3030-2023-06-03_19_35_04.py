a = input().split(',')
b = input().split(',')
ls = []
for i in range(len(a)):
    ls.append([a[i],int(b[i]]))
ls.sort(key = lambda x : x[1])
print(ls)


