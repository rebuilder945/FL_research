n = input()
flag = False
for x in range(100,min(1000,eval(n)+1)):
    if int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3 == x:
        print(x)
        flag = True
if flag == False:
    print('none')


