a=input()
if len(a)!=18:
    print("False")
num={0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
s=int(a[0])*7+int(a[1])*9+int(a[2])*10+int(a[3])*5+int(a[4])*8+int(a[5])*4+int(a[6])*2+int(a[7])*1+int(a[8])*6+int(a[9])*3+int(a[10])*7+int(a[11])*9+int(a[12])*10+int(a[13])*5+int(a[14])*8+int(a[15])*4+int(a[16])*2
n=s%11
p=num.get(n)
if p==a[17]:
    print("Correct")
else:
    print("Wrong")
