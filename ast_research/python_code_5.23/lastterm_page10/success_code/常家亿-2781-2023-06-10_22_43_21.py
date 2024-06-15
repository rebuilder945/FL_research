a=input()
lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
lst2=[0,1,2,3,4,5,6,7,8,9,10]
lst3=[1,0,'X',9,8,7,6,5,4,3,2]
s=0
if len(a)!=18:
    print('Wrong')
else:
    for i in range(0,17):
        for j in range(0,17):
            if i==j:
                s=s+int(a[i])*lst1[j]
    yu=s%11
    m=(12-yu)%11
    if yu in lst2:
        q=lst2.index(yu)
        if lst3[q]==a[17]:
            print('Correct')
        else:
            print('Wrong')
    else:
        print('Wrong')
    

