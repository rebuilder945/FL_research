a=int(input())
red={1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
green={0}
black={2,4,6,8,10,11,13,15,17,20,22,254,26,28,29,31,33,35}
if a in red:
    print('red')
elif a in green:
    print('green')
elif a in black:
    print('black')
else:
    print('error')

