a=eval(input())
b=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
c=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
if a not in range(37):
    print('error')
if a in b:
    print('red')
if a in c:
    print('black')
if a==0:
    print('green')
