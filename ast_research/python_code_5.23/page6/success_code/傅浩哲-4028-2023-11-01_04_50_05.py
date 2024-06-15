a=eval(input())
if a<0 or int(a)!=a:
    print('illegal input')
else:
    for i in range(2,a+1):
        if i==i.reverse():
            for j in range(2,i):
                if i%j!=0:
                    continue
            else:
                print(i,end='')
