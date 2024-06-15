num=input()
p1=[]
p2=[]
p3=[]
p4=[]
s1="0123456789"
s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s3="abcdefghijklmnopqrstuvwxyz"
s4="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
if len(num)>=8:
    a=1
else:
    a=0
for i in num:
    if i in s1:
        p1.append(i)
    if i in s2:
        p2.append(i)
    if i in s3:
        p3.append(i)
    if i in s4:
        p4.append(i)
if p1!=[]:
    a+=1
if p2!=[]:
    a+=1
if p3!=[]:
    a+=1
if p4!=[]:
    a+=1
print(a)
