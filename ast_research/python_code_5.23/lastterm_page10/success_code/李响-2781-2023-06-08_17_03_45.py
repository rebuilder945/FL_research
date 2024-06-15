a = list(input())
b = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(a) != 18:
    print('Error')
else:   
    s = 0
    for i in range(len(b)):
        s = s + int(a[i])*b[i]
n = s%11
m = (12-n)%11
if a[-1] == 'X':
    if m == 10:
        print('Correct')
    else:
        print('Wrong')
else:
    if m == int(a[-1]):
        print('Correct')
    else:
        print('Wrong')
