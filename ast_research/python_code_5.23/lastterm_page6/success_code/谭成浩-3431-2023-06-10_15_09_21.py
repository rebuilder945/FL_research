x1=[0]
x2=[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
x3=[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
n=eval(input())
if n not in range(0,37):
    print('error')
elif n in x1:
    print('green')
elif n in x2:
    print('red')
elif n in x3:
    print('black')
    
