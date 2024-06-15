l=list(input())
l1=[]
for i in l:
    if i =='X':
        l1.append(10)
    else:
        l1.append(int(i))
l2=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum=0
if len(l1)==18:
    for i in range(17):
        sum+=l1[i]*l2[i]
    n=sum%11
    m=(12-n)%11
    if m==l1[-1]:
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')
