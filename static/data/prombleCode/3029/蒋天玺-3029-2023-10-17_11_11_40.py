a = input()
n = ''
name = []
for x in a :
    if x == ',':
        name.append(n)
        n = ''
        continue
    n = n + x
name.append(n)
grade = eval(input())
new= []
for i in range(len(grade)):
    temp = [name[i],grade[i]]
    new.append(temp)
print(new)




