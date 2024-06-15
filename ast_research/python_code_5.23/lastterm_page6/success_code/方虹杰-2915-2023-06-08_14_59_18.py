a=input()
if eval(a)<=100:
    print('none')
elif eval(a)<1000:
    for i in range(100,eval(a)):
        b=list(str(i))
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==i:
            print(i)
else:
    for i in range(100,1000):
        b=list(str(i))
        if int(b[0])**3+int(b[1])**3+int(b[2])**3==i:
            print(i)
