a=int(input())
if a<0 or a>36:
    print('error')
elif a==0:
    print('green')
elif a in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
    print('red')
else:
    print('black')

