
a = eval(input())
for i in range(100,a+1):
    if i==int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3:
        print(i)
else:
    print('None')

        

