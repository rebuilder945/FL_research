lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
n=input()
c=0
for i in range(0,17):
    c+=lst1[i]*int(n[i])
yu=c%11
lst2=[0,1,2,3,4,5,6,7,8,9,10]
lst3=[1,0,'X',9,8,7,6,5,4,3,2]
x=lst2.index(yu)
if str(n[-1])==str(lst3[x]):
    print('Correct')
else:
    print('Wrong')
