n=list(input())
s=''
for i in n:
    if n.count(i)==1:
        s+=i
    a=s
if a=='':
        print("None")
else:
        print(s[0])
        



