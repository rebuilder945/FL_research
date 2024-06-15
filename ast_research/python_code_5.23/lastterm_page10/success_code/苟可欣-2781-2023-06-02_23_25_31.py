def yu(a):
    for x in a[:-1]:
        ls.append(int(x))
    a=7*ls[0]+9*ls[1]+10*ls[2]+5*ls[3]+8*ls[4]+4*ls[5]+2*ls[6]+1*ls[7]+6*ls[8]+3*ls[9]+7*ls[10]+9*ls[11]+10*ls[12]+5*ls[13]+8*ls[14]+4*ls[15]+2*ls[16]
    n=a%11
    m=(11-n)%11
    if m==10:
        if a[-1]=="X":
            print("Correct")
        else:
            print("Wrong")
    else:
        if a[-1]=="m":
            print("Correct")
        else:
            print("Wrong")
a=input()
ls=[]
if len(a)!=18:
    print("Error")
else:
    yu(a)
