name = input().split(',')
grade = eval(input())
ls = []
for i in range(len(name)):
    a = [name[i],grade[i]]
    ls.append(a)
print(ls)
