a=input()
c=0
for x in a:
    b=a.count(x)
    if b==1:
        c+=1
        print(x)
        break
if c==0:
    print('None')
