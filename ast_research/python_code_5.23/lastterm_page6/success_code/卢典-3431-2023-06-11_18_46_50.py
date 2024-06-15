x=eval(input())
lis1=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
if x not in range(0,37):
    print('error')
else:
    if x==0:
        print('green')
    elif x in lis1:
        print('red')
    else:
        print('black')
