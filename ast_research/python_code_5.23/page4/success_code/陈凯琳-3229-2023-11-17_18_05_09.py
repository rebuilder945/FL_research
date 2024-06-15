a=eval(input())
lit=[]
for i in a:
    b=a.count(i)
    if b==1:
        lit.append(str(i))
lit.sort()
if lit==[]:
    print('False')
else:
    print(','.join(lit))





     

    


