a = eval(input())
r = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
b = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
if a == 0:
    print('green')
elif a in r:
    print('red')
elif a in b:
    print('black')
else:
    print('error')
