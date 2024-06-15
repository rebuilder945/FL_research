name = input().spilt(',')
score = list(map(int,input().spilt(',')))
ls = []
for i in range(len(name)):
    ls.append([name[i],score[i]])
# print(ls)
ls.sort(key=lambda x: x[1])
print(ls)
