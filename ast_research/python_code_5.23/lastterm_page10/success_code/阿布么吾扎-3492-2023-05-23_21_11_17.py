a=input()
if len(a)==0:
    print('None')
for x in a:
    if a.count(x)==1:
        print(x)
        break
    
