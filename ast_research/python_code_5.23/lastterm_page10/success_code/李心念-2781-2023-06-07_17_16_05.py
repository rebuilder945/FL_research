m = input()
s = list(m)
if len(s) != 18:
    print('Error')
else:
    num = list(map(int,s[:-1]))
    n = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    a1 = 0
    for x in range(17):
        a1 += num[x]*n[x]
    a1 = a1%11
    a = (12-a1)%11
    b = s[-1]
    if (b == 'X' and a == 10) or (type(b)==int and int(b) == a):
        print('Correct')
    else:
        print('Wrong')
