coefficient=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
lst=list(input())
length=len(lst)
code=lst.pop()
lst1=list(map(int,lst))
sum=0
if length!=18:
    print('Error')
else:
    for i in range(17):
        sum+=coefficient[i]*lst1[i]
    mod=sum%11
    if code=='X' and (12-mod)%11==10:
        print('Correct')
    elif code.isdigit() and (12-mod)%11==int(code):
        print('Correct')
    else:
        print('Wrong')
