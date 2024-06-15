n=eval(input())
a=[0]
b=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
c=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
if n in a:
    print('green')
elif n in b:
    print('red')
elif n in c:
    print('black')
else:
    print('error')
