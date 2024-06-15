


a=eval(input())
if a<0 or int(a)!=a:
    print("illegal input")
else:
    for i in range(1,a+1):
        for j in range(2,i):
            if i%j==0:
                break
            else:
                print(i,end='')
