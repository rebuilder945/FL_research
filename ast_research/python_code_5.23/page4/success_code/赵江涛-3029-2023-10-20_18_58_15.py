name = input()
grade = eval(input())
ls = []
for i in range(len(grade)):
    ls.append(name[i-1])
    ls.append(grade[i-1])
    print(ls)

