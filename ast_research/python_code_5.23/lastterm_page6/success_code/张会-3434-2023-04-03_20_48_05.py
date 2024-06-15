lst =['red','blue','yellow']
yuanse1 = input()
yuanse2 = input()
s = {yuanse1,yuanse2}
chengse1 = {'red','blue'}
chengse2 = {'red','yellow'}
chengse3 = {'blue','yellow'}
a = ''
if yuanse1 not in lst or yuanse2 not in lst:
    print('error')
else:
    if yuanse1 == yuanse2:
        print('error')
    else:
        if s == chengse1:
            print('purple')
        elif s == chengse2:
            print('orange')
        else:
            print('green')
    

