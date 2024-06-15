n1=list(input())
n2=list(input())
dit1={}
dit2={}
for x in n1:
    dit1[x]=dit1.get(x,0)+1
for x in n2:
    dit2[x]=dit2.get(x,0)+1
if dit1==dit2:
    print('True')
else:
    print('False')



      
