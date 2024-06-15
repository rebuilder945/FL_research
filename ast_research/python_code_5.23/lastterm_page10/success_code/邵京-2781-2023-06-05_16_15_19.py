number=input().split()
numberlist=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
code=[1,0,'X',9,8,7,6,5,4,3,2]
if len(number)!=18:
    print('Error')
else:
    for i in range(18):
        a=sum(int(number[i])*numberlist[i])
        b=a%11
        if code[b]==number[17]:
            print('Correct')
        else:
            print('Wrong')    






