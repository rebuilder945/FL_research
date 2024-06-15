str1 = input()
name = [str(x) for x in str1.split(',')]
grade = eval(input())
l = len(grade)
lst = []
lst1 = []
for i in range(l):
   lst.append(name[i]+grade[i])
   lst1.append(lst)
   lst = []
print(lst1)
