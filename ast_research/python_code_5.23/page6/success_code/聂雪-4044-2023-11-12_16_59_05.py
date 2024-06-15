a = eval(input())
ls=[]
for i in range(100,a+1):
    if i==int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3:
        ls.append(i)
if len(ls)==0:
    print('None')
else:
    for x in ls:
        print(x)
        

