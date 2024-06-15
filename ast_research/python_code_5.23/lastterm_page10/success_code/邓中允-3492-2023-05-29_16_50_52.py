s=input()
a=[]
if s=="":
    print("None")
else:
    for i in range(len(s)):
        if s.count(i)==1:
            a.append(s[i])
print(a[0])

