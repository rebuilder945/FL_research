a = eval(input())
ls = []
for i in range(a):
    if len(str(i))==3:
        if (int(str(i)[0]))**2+(int(str(i)[1]))**2+(int(str(i)[2]))**2==i**2:
            print(i)
            ls.append(i)
if  not ls:
    print('none')


