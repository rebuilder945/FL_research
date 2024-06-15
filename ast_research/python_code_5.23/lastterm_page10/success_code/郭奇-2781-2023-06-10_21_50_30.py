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
    dic={0:1,1:0,2:'X',3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2}
    if dic[m]==lst[-1]:
        print('Correct')
    else:
        print('Wrong')

