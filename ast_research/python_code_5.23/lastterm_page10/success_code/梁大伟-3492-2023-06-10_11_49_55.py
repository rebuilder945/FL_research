s=input() or 'None'
if s !='None':
    for i in s:
        if s.count(i)==1:
            print(i)
            break
else:
    print('None')
