a=str(input())
if a =='':
    print('None')
else:
    lst=list(a)
    for i in lst:
        n=lst.count(i)
        if n==1:
            print(i)
            break

