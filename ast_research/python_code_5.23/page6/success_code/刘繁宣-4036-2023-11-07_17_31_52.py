n = eval(input())
if 1<= n <11 and n%2 !=0:
    print('red')
elif 11<= n <19 and n%2==0:
    print('red')
elif 19<= n <29 and n%2!=0:
    print('red')
elif 29<= n <=36 and n%2==0:
    print('red') 
elif n==0:
    print('green')
elif n<0 or n>36:
    print('error')
else:
    print('black')   
