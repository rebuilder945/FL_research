name = input().split(',')
name = list(name)
scores = eval(input())
ls = []
for x in range(len(name)):
    a = []
    a.append(name[x])
    a.append(scores[x])
    ls.append(a)
print(ls)



