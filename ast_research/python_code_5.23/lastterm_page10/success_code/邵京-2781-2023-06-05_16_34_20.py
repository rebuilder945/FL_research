number=input()
numberlist=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
code=[1,0,'X',9,8,7,6,5,4,3,2]
if len(number)!=18:
    print('Error')
else:
        list=[]
        for i in range(len(number)-1):
             list.append(int(number[i]))
        a=list[0]*7+list[1]*9+list[2]*10+list[3]*5+list[4]*8+list[5]*4+list[6]*2+list[7]*1+list[8]*6+list[9]*3+list[10]*7+list[11]*9+list[12]*10+list[13]*5+list[14]*8+list[15]*4+list[16]*2
        b=a%11
        if code[b]==number[17]:
            print('Correct')
        else:
            print('Wrong')    






