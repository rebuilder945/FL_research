s=str(input())
ls=[]
if s=='':
    print('None')
else:
    ls1=s.split()
    for i in ls1:
        if ls1.count(i)==1:
            print(i)
            break

