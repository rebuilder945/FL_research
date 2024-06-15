s = []
num = eval(input())
for i in range(100,num+1):
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        s.append(i)
if s == []:
    print('none')
else:
    print(s)
