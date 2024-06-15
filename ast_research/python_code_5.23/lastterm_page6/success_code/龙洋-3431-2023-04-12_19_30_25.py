red=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
lis=[x for x in range(37)]
x=eval(input())
if x==0:
    print('green')
elif x in red:
    print('red')
elif not x in lis:
    print('error')
else:
    print('black')
