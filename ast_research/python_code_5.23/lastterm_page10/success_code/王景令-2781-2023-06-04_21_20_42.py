a = input()
c = 0
d = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
if len(a) != 18 :
    print('Error')
else:
    for i in range(len(a) - 1):
        c += int(a[i])*d[i]
    n = c % 11
    m = (12-n) % 11
    if a[-1] == 'X':
        if m == 10:
            print('Correct')
        else:
            print('Error')
    else:
        if m == eval(a[-1]):
            print('Correct')
        else:
            print('Error')
    
