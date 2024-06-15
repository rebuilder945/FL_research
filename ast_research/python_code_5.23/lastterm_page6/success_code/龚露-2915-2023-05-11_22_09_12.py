a = eval(input())
num=[]
if a <= 100:
    print('none')
else:
    for i in range(100,a+1):
        b = str(i)[0]
        c = str(i)[1]
        d = str(i)[2]
        if int(b)**3 + int(c)**3 +int(d)**3 ==i and len(str(i))==3:
            num.append(i)
        final = ",".join(str(x) for x in num)
    print(final)

