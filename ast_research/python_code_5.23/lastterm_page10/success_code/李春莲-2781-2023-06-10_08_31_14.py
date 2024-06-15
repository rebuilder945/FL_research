l=list(input())
l1=[]
for i in l:
    if i =='X':
        l1.append(10)
    else:
        l1.append(int(i))
l2=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum=0
for i in range(17):
    sum+=l1[i]*l2[i]
    n=sum%11
    m=(12-n)%11
if len(l1)==18:
    if (n==0 and m==1) or (n==1 and m==0) or (n==2 and m==10) or (n==3 and m==9) or (n==4 and m==8) or (n==5 and m==7) or (n==6 and m==6) or (n==7 and m==5) or (n==8 and m==4) or (n==9 and m==3) or (n==10 and m==2):
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')
