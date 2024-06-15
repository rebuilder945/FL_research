p1_lst=[]
p2_lst=[]
p3_lst=[]
p4_lst=[]
nums=input()
if len(nums)>=8:
    d=1
else:
    d=0
for x in nums:
    if x in "0123456789":
        p1_lst.append(x)
    elif x in "abcdefghijklmnopqrstuvwxyz":
        p2_lst.append(x)
    elif x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        p3_lst.append(x)
    elif x in "~!@#$%^&*()_=-/,.?<>;{\:[}]|" :
        p4_lst.append(x)
if len(p1_lst)!=0:
    d+=1
elif len(p2_lst)!=0:
    d+=1
elif len(p3_lst)!=0:
    d+=1
elif len(p4_lst)!=0:
    d+=1
print(d)
