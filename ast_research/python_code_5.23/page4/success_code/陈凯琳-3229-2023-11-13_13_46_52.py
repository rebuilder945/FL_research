lit1=eval(input())
lit=[]
for i in lit1:
    if lit1.count(i)==1:
        lit.append(str(i))
lit.sort()
if lit==[]:
   print('False')
else:
   print(','.join(lit))



