num = int(input())
flag = False
if num<100:
    flag = False
else:
    for i in range(100,num+1):
        a = i//100
        b = (i//10)%10
        c = i%10
        if i == a**3+b**3+c**3:
            print(i)
            flag = True
        if i == 999:
            break
if(flag == False):
    print('none')

