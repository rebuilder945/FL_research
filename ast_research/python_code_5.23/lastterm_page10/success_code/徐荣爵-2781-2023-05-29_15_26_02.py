s1 = input()
if len(s1) != 18:
    print('Error')
else:
    num = 0
    lst = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    lst2 = [1,0,'X',9,8,7,6,5,4,3,2]
    for i in range(len(lst2)):
        lst2[i] = str(lst2[i])

    for i in range(len(s1)-1):
        num += int(s1[i]) * int(lst[i])
    ln = num % 11
    d = dict([])
    for i in range(11):
        d[i] = lst2[i]
    p = d.get(ln)
    if p == s1[-1]:
        print('Correct')
    else:
        print('Wrong')
