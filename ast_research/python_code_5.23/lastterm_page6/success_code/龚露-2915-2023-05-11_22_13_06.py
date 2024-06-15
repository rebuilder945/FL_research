a = eval(input())
x = 1
for i in range(100,a+1):
    b = str(i)[0]
    c = str(i)[1]
    d = str(i)[2]
    if int(b)**3 + int(c)**3 +int(d)**3 ==i and len(str(i))==3:
        print(i)
        x = 0
    else:
        pass
if x == 1:
    print('none')



