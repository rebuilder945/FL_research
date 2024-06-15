n = eval(input())
ls=[]
for i in range(n+1):
    if 1000>i>100:
        if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
            ls.append(i)
            print(i)
if len(ls)==0:
    print('none')
