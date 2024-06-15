a=input()
count=0
length=0
temp=[]
dig=[]
for i in a:
    if i.isdigit():
        count+=1
        temp.append(i)
    else:
        if count>=length:
            length=count
            count=0
            dig=temp.copy()
            temp=[]
        else:
            temp=[]
            count=0
if len(temp)>=len(dig):
    result="".join(temp)
else:
    result="".join(dig)
if len(result)>0:
    print(result)
else:
    print("No digits")    

        

    



