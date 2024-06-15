str1 = input()
name = [str(n) for n in str1.split(',')]
grade = eval(input())
jishu = 0
x2 = []
long = len(name)
while long>0:
    x1 = []
    x1.append(name[jishu])
    x1.append(grade[jishu])
    x2.append(x1)
    jishu += 1
    long -=1
x3 = sorted(x2,key=lambda x:x[1])
print(x2)
