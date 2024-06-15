a = eval(input())
ls = []
for i in range(153,a+1):
    if len(str(i))==3:
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3 == i:
            print(i)
            ls.append(i)
if not ls:
    print('none')



