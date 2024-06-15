a=input()
if a=='':
    print('None')
else:
    b=list(a)
    for i in b:
        if i.isalpha():
            if b.count(i)==1:
                print(i)
                break
