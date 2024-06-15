line=input()
count=0
length=0
temp=[]
dig=[]
for ch in line :
    if (ch>='0'and ch <='9'):
        count+=1
        temp.append(ch)
    else:
        if count>=length:
            length=countcount=0
            dig =temp.copy()
            temp=[]
        else:
            temp=[]
            count=0
if len(temp)>=len(dig):
    result=''.join(temp)
else:
    result=''.join(dig)
if len(result)>0:
    print(result)
else:
    print("No digits")
