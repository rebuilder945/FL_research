a=int(input())
for b in range(100,a+1):
    A=b[0]
    B=b[1]
    C=b[2]
    if A**3+B**3+C**3==int(b):
        print('\nb')
    else:
        print('none')
