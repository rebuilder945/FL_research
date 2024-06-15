str1 = input()
name = [str(s) for s in str1.split(',')]
grade = eval(input())
lst = []
for i in range(len(name)):
    group = (name[i],grade[i])
    ls = list(group)
    lst.append(ls)

print(lst)

