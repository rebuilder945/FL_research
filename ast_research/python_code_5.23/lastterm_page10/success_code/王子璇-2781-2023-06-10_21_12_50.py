# icards=input()
# if len(icards)!=18:
#     print('Error')
# elif len(icards)==18:
#     lst1=[int(x) for x in icards[:17]]
#     n=(lst1[0]*7+lst1[1]*9+lst1[2]*10+lst1[3]*5+lst1[4]*8+lst1[5]*4+lst1[6]*2+lst1[7]*1+lst1[8]*6/
#        lst1[9]*3+lst1[10]*7+lst1[11]*9+lst1[12]*10+lst1[13]*5+lst1[14]*8+lst1[15]*4+lst1[16]*2)%11
#     m=(12-n)%11
#     if str(m)!=icards[-1] and m!=10:
#         print("Wrong")
#     if m==10 and icards[-1]=="X":
#         print("Correct")
#     if m!=10 and str(m) ==icards[-1]:
#         print("Correct")
#     if m==10 and icards[-1]!="X":
#         print("Wrong")
icards=input()
if len(icards)!=18:
    print("Error")
elif len(icards)==18:
    lst1=list(eval(x) for x in icards[0:17])
    n=(lst1[0]*7+lst1[1]*9+lst1[2]*10+lst1[3]*5+lst1[4]*8+lst1[5]*4+lst1[6]*2+lst1[7]*1+lst1[8]*6+lst1[9]*3+lst1[10]*7+lst1[11]*9+lst1[12]*10+lst1[13]*5+lst1[14]*8+lst1[15]*4+lst1[16]*2)%11
    m=(12-n)%11
    if str(m)!=icards[-1] and m!=10:
        print("Wrong")
    if m==10 and icards[-1]=="X":
        print("Correct")
    if m!=10 and str(m) ==icards[-1]:
        print("Correct")
    if m==10 and icards[-1]!="X":
        print("Wrong")

