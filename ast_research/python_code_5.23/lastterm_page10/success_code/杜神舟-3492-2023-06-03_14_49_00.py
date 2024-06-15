a=input()
b=a.split()
for x in b:
    if a.count(x)==1:
        print(x)
        break
    else:
        print('None')
        break
