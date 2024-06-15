s=input()
a=[]
for i in range(len(s)):
    b=s.count(s[i])
    if b==1:
        a.append(s[i])
if len(a)==0:
    print("None")
else:

    print(a[0])
    
