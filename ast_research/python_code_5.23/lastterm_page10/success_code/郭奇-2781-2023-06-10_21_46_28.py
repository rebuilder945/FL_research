a=input()
lst=list(a)
if len(lst)!=18:
    print('Error')
else:
    lst1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    c=0
    for i in range(17):
        c+=int(lst[i])*lst1[i]
    y=c%11
    m=(12-y)%11
    lst2=[1,0,'X',9,8,7,6,5,4,3,2]
    if lst2[m]==lst[-1]:
        print('Correct')
    else:
        print('Wrong')

