def s(x):
    if int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3==x:
        return True
    else:
        return False
x=eval(input())
b=[]
for i in range(100,x+1):
    if s(i)==True:
        b.append(i)
if b!=[]:
    for i in range(len(b)):
        print(b[i])
else:
    print('none')


