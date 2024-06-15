str1 = input()
name = [str(s) for s in str1.split(',')]
grade = eval(input())
lst = []
for i in range(len(name)):
    ls = list(name[i],grade[i])
    lst.append(ls)

print(lst)

