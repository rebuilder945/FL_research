ind = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
idi = input()
c = 0
for i in range(len(idi)-1):
    c += int(idi[i])*ind[i]
if len(idi) == 18:
    d = c % 11
    if idi[-1] != 'X':
        if d + int(idi[-1]) == 12 or d + int(idi[-1]) == 1:
            print('Correct')
        else:
            print('Wrong')
    else:
        if d + 10 == 12:
            print('Correct')
        else:
            print('Wrong')
else:
    print('Error')

