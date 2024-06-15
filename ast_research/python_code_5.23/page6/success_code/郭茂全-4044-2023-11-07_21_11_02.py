a=eval(input())
s=0
for x in range(100,min(a+1,1000)):
    if int(str(x)[0])+int(str(x)[1])+int(str(x)[2])==x:
        print(x)
else:
    print('none')
