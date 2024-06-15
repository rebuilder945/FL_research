a = eval(input())
if type(a) == type(1.1) or a<= 1:
    print('illegal input')
else:
    for i in range(2,a+1):
        if str(i)[0] == str(i)[-1]:
            for x in range(2,i):
                if i%x == 0:
                    break
                else:
                    print(i,end = '')


