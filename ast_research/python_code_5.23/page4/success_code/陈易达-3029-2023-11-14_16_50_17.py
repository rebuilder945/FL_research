names = input().split(',')
scores = eval(input())
ls = []
for x in range(len(scores)):
    ls.append([names[x],scores[x]])
print(ls)
