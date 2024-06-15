a=input()
s=1
for i in a:
    if a.count(i)>1:
        continue
    else:
        print(i)
        s=0
        break
if s==1:
    print('None')
