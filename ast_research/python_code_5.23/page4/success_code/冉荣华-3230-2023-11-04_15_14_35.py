x=eval(input())
x.sort(reverse=True)
if max(x)!=0:
    for i in range(len(x)):
        print(x[i],end='')
else:
    print('0')


