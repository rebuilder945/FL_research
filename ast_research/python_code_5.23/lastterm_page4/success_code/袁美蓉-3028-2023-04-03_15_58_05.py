name = input().split(',')
score = list(map(int,input().split(',')))
ls = []
for i in range(len(name)):
    ls.append([name[i],score[i]])
print(ls)

