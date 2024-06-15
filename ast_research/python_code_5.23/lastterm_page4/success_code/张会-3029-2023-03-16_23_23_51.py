name = input().split(",")
score = eval(input())
l = len(name)
l = len(score)
a = name[0]
b = score[0]
c = [a,b]
ls = [c]
for i in range(1,l):
    ls.append([name[i],score[i]])
print(ls)

