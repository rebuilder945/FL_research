def proof(a):
    str=[]
    for i in a:
        str.append(i)
    if str[-1]=="X":
        str[-1]="10"
    str=list(map(int,str))
    sum=str[0]*7+str[1]*9+str[2]*10+str[3]*5+str[4]*8+str[5]*4+str[6]*2+str[7]*1+str[8]*6+str[9]*3+str[10]*7+str[11]*9+str[12]*10+str[13]*5+str[14]*8+str[15]*4+str[16]*2
    n=sum % 11
    m=(12-n) % 11
    if m==str[-1]:
        return "Correct"
    else:
        return "Wrong"
str=input()
if len(str)!=18:
    print("Error")
else:
    print(proof(str))
