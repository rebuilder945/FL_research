p1_list=[]
p2_list=[]
p3_list=[]
p5_list=[]
p=input()
if len(p)>=8:
    d=1
else:
    d=0
for x in p:
    if x in "1234567890":
        p1_list.append(x)
    elif x in "abcdefghijklmnopqrstuvwxyz":
        p2_list.append(x)
    elif x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        p3_list.append(x)
    elif x in "~!@#$%^&*()_=-/,.?<>\;:[}]{|":
        p5_list.append(x)
if len(p1_list)!=0:
    d+=1
if len(p2_list)!=0:
    d+=1
if len(p3_list)!=0:
    d+=1
if len(p5_list)!=0:
    d+=1
print(d)

