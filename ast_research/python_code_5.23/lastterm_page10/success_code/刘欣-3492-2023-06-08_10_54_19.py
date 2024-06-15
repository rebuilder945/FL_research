strs=input()
if strs=='':
    print('None')
else: 
    for i in strs:
        if strs.count(i)==1:
            print(i)
            break

