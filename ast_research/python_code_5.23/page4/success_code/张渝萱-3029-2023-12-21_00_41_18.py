str1 = input()
# Very important!!!
name = [str(n) for n in str1.split(',')]
grade = eval(input())
length = len(name)
count = 0
x2 = []
while length>0:
    x1 = []
    x1.append(name[count])
    x1.append(grade[count])
    x2.append(x1)
    count += 1
    length -= 1
print(x2)
