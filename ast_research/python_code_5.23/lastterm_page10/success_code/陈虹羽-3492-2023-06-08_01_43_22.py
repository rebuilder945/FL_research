a=input()
if a=='':
    print('None')
else:
    for i in a:
        b=a.count(i)
        if b==1:
            print(i)
           
            break
