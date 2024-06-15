a=input()
c=0
for x in a:
    b=a.count(x)
    if b==1:
        print(x)
        c=1
        break
if c==0 or a=='':
    print('None')
